from django.contrib.auth.models import AbstractUser
from django.db import models 
from uuid import uuid4
from datetime import datetime
import os

class User(AbstractUser):    

    email = models.EmailField(        
        max_length=255,        
        unique=True,    
    )    
    username = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )     
    date_joined = models.DateTimeField(auto_now_add=True)  
    is_clerk = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'    
    REQUIRED_FIELDS = ['email']



def uuid_name_upload_to(instance, filename):
    ymd_path = datetime.now().strftime('%Y/%m/%d')  # 업로드하는 년/월/일 별로
    uuid_name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()  # 확장자 추출하고, 소문자로 변환
    return '/'.join([
        ymd_path,
        uuid_name[:2],
        uuid_name + extension,
    ])

class PictureRequest(models.Model):
    clerk = models.ForeignKey(User, related_name="request_clerk", on_delete=models.CASCADE, blank=True, null=True)
    customer = models.ForeignKey(User, related_name="request_customer", on_delete=models.CASCADE, blank=True, null=True)
    #image = models.ImageField(upload_to=uuid_name_upload_to, null=True, blank=True, verbose_name="고객사진")
    image = models.FileField(upload_to=uuid_name_upload_to, blank=True, verbose_name="고객 사진")
    uploaded = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)