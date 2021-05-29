from django.contrib import admin
from django.urls import path
from .views import *

app_name = "PictureHandler"

urlpatterns = [
    path('encrypt/<int:pk>', send_to_encryptor, name="picture_handler_encryptor"),
    path('decrypt/<int:pk>', send_to_decryptor, name="picture_handler_decryptor"),
    path('picturedelete/<int:pk>', picture_delete, name="picture_delete"),
]
