from django.shortcuts import render, get_object_or_404, redirect
from Clerk.forms import PictureRequestForm
from Clerk.models import PictureRequest
from .utils import *
from IEP.settings import BASE_DIR
from IEP.settings import MEDIA_ROOT

# Create your views here.

def send_to_encryptor(request, pk):
    picture_request = get_object_or_404(PictureRequest, pk=pk)
    #target = PictureEncryptor.encrypt_image(os.path.join(".", MEDIA_ROOT, picture_request.image.url), 1)
    target = PictureEncryptor.encrypt_image(picture_request.image.url, 1)

    picture_request.image = target
    picture_request.save()

    return redirect('Customer:customer_home')


def picture_delete(request, pk):
    DataBaseConnector.delete_complete_request(pk)
    return redirect("Clerk:clerk_home")