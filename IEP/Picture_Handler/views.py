from django.shortcuts import render, get_object_or_404, redirect
from core.forms import PictureRequestForm
from core.models import PictureRequest
from .utils import *
from IEP.settings import BASE_DIR
from IEP.settings import MEDIA_ROOT

# Create your views here.


def send_to_encryptor(request, pk):
    picture_request = get_object_or_404(PictureRequest, pk=pk)
    PictureHandler.encrypt(picture_request)

    return redirect('Customer:submit_success')

def send_to_decryptor(request, pk):
    picture_request = get_object_or_404(PictureRequest, pk=pk)

    target = PictureHandler.decrypt(picture_request)
    picture_request.image = target
    picture_request.save()
    context = {
        "picture_request" : picture_request
    }

    return render(request, "Clerk/send_to_decryptor.html", context=context) 



def picture_delete(request, pk):
    DataBaseConnector.delete_complete_request(pk)
    return redirect("Clerk:clerk_home")