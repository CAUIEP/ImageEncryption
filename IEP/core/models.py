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