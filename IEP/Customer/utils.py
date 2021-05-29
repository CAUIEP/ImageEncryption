from django.contrib import messages
from core.models import User
from core.models import PictureRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from core.forms import PictureRequestForm

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

class Discrimiator:

    @classmethod
    def get_form_POST(cls, request, instance):
        return PictureRequestForm(request.POST, request.FILES, instance)

    @classmethod
    def get_form_GET(cls, instance):
        return PictureRequestForm(instance)

class Upload:
    @classmethod
    def upload(cls, request, picture_request, clerk, customer, form, pk):
            picture_request.clerk = clerk
            picture_request.customer = customer
            picture_request.uploaded = True
            picture_request = form.save()
            picture_request.image = request.FILES.get('image')
            return redirect('PictureHandler:picture_handler_encryptor', pk)
