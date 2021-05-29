from django.contrib import messages
from core.models import User
from core.models import PictureRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

class PageMaker:    
    @classmethod
    def get_page(cls, request, template_name, context=None):
        return render(request, template_name, context)

class AlarmOperator:
    @classmethod
    def activate(cls, request, message):
        return messages.add_message(request, messages.INFO, message)

class DBConnector:
    @classmethod
    def get_request_all(cls, request):
        return PictureRequest.objects.filter(customer=request.user, uploaded = False)

    @classmethod
    def get(cls):
        return