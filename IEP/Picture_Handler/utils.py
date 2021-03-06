from Crypto.Cipher import AES
import PIL.Image
import os
import hashlib
from core.models import PictureRequest
from IEP.settings import BASE_DIR
from IEP.settings import MEDIA_ROOT
import io
from django.shortcuts import render, get_object_or_404, redirect

class PictureHandler:
    key = None
    file = None

    @classmethod
    def flush(cls):
        cls.key = None
        cls.file = None

    @classmethod
    def need_a_key(cls, request_info):
        cls.key = KeyHandler.key_generate(request_info)

    @classmethod
    def encrypt(cls, request_info):
        cls.need_a_key(request_info)
        if cls.key != False:
            file = PictureEncryptor.encrypt_image(request_info.image.url, cls.key)

        cls.flush()
        DataBaseConnector.store(request_info, file)
    
    @classmethod
    def decrypt(cls, request_info):
        cls.need_a_key(request_info)
        if cls.key != False:
            file = PictureDecryptor.decrypt_image(request_info.image, cls.key)
        cls.flush()
        return file



class KeyHandler:
    @classmethod
    def send_key(cls, key):
        if key:
            return key
        else:
            return False

    @classmethod
    def key_generate(cls, request_info):
        if Checker.is_valid(request_info):
            #generating key
            key = request_info.customer.id + request_info.clerk.id + int(request_info.created_at.toordinal())
            return cls.send_key(str(key))
        else:
            return cls.send_key(False)

class Checker:
    #class diagram 에서 request_id 를 아마 삭제해도 될 것 같음
    @classmethod
    def get_request_info(cls, request_id):
        return DataBaseConnector.get_send_info(request_id)
    
    @classmethod
    def is_valid(cls, request_id):
        request_info = cls.get_request_info(request_id)
        if request_info:
            if request_info.customer and request_info.clerk and request_info.created_at:
                return True
        return False


class PictureEncryptor:
    @classmethod
    def encrypt_image(cls, image, key_value):

        #Just for debugging need to delete
        key_value = key_value.encode()
        digest = hashlib.md5(key_value).digest() # 16 byte binary

        key = digest
        iv=b'0000000000000000'

        image_path = image[1:]

        input_file = open(image_path, 'rb')
        input_data = input_file.read()
        input_file.close()

        cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
        enc_data = cfb_cipher.encrypt(input_data)

        encrypt_file = image_path.split(".")
        encrypt_file = encrypt_file[:-1][0] + ".enc"

        with open(encrypt_file, 'wb') as f:
            f.write(enc_data)

        cls.delete_local_encrypted_file(image_path)

        return encrypt_file

    @classmethod
    def delete_local_encrypted_file(cls, image):
        os.remove(image)



class PictureDecryptor:
    @classmethod
    def decrypt_image(cls, image, key_value):
        key_value = key_value.encode()
        digest = hashlib.md5(key_value).digest() # 16 byte binary

        key = digest
        iv=b'0000000000000000'

        image = str(image)
        try:
            enc_file2 = open(image,"rb")
        except:
            return image
        
        enc_data2 = enc_file2.read()
        enc_file2.close()
        cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
        plain_data = (cfb_decipher.decrypt(enc_data2))

        decrypt_file = image.split(".")
        decrypt_file = decrypt_file[:-1][0] + ".jpg"
        imageStream = io.BytesIO(plain_data)
        try:
            #파일이 열리는 지 확인하는 메서드 
            imageFile = PIL.Image.open(imageStream)
        except:
            return False
        cls.delete_local_encrypted_file(image)
        imageFile.save(decrypt_file)
        decrypt_file = "/".join(decrypt_file.split("/")[1:])
        return decrypt_file

    @classmethod
    def delete_local_encrypted_file(cls, image):
        os.remove(image)



class DataBaseConnector:
    @classmethod
    def get_send_info(cls, request_info):
        try:
            information = PictureRequest.objects.get(pk = request_info.pk)
        except:
            return False
        return information

    @classmethod
    def store(cls, request_info, file):
        picture_request = get_object_or_404(PictureRequest, pk = request_info.pk)
        picture_request.image = file
        picture_request.save()

    @classmethod
    def delete_complete_request(cls, pk):
        picture_request = get_object_or_404(PictureRequest, pk = pk)
        picture_request.delete()