from Crypto.Cipher import AES
import PIL.Image
import os
import hashlib
from Clerk.models import PictureRequest
from IEP.settings import BASE_DIR
from IEP.settings import MEDIA_ROOT
import io

class PictureEncryptor:
    @classmethod
    def encrypt_image(cls, image, key):

        #Just for debugging need to delete
        key_value = '1'
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

        os.remove(image_path)

        return encrypt_file


class PictureDecryptor:
    #Decrypting Image
    @classmethod
    def decrypt_image(cls, image, key):
        key_value = '1'
        key_value = key_value.encode()
        digest = hashlib.md5(key_value).digest() # 16 byte binary

        key = digest
        iv=b'0000000000000000'

        image = str(image)
        enc_file2 = open(image,"rb")
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

        os.remove(image)

        imageFile.save(decrypt_file)

        decrypt_file = "/".join(decrypt_file.split("/")[1:])

        print(decrypt_file)

        return decrypt_file