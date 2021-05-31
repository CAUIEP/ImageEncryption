
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls import url

app_name = 'Clerk'
urlpatterns = [
    path('', clerk_home,name="clerk_home"),
    path('create/', select_customer, name="select_customer"),
    path('create/select/<str:customer_name>', select_document_view.as_view(), name = "select_document"),
    path("signup/", sign_up, name="signup"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path('rlist/', picture_request_list, name="picture_request_list"),
    path('download/<int:pk>', picture_download, name="picture_download"),
    path('decryptor/<int:pk>', picture_decryptor, name="send_to_decryptor")
]
