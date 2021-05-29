
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls import url

app_name = 'Clerk'
urlpatterns = [
    path('create/', select_customer, name="select_customer"),
    # path('create/select', select_documet,name = "select_documet"),
    # url(r'^create/select/(?P<customer_name>[a-z]+)/$', select_documet,name="select_document"),
    path('create/select/<str:customer_name>', select_document_view.as_view(), name = "select_document"),
    path('', clerk_home,name="clerk_home"),
    path("signup/", sign_up, name="signup"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
]
