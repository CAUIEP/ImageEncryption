from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'Customer'
urlpatterns = [
    path('', customer_home, name="customer_home"),
    path("signup/", sign_up, name="signup"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
]