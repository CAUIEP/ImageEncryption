from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'Customer'
urlpatterns = [
    path('', customer_home, name="customer_home"),
    path('confirm/', customer_confirm, name="customer_confirm"),
    path('detail/<int:pk>/', customer_read, name="customer_read"),
    path('upload/<int:pk>/', picture_upload, name="picture_upload"),
    path("signup/", sign_up, name="signup"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
]