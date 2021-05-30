from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from core.models import User
from core.forms import *
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .utils import *
from django.contrib import messages


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_customer = True
            user.save()
            return redirect("Customer:customer_home")
        else:
            ctx = {
                "form": form,
            }
            return render(request, "customer/sign_up.html", ctx)

    elif request.method == "GET":
        form = SignUpForm()
        ctx = {
            "form": form,
        }
        return render(request, "customer/sign_up.html", ctx)

def login(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)

            return redirect("Customer:customer_home")
        else:
            ctx = {
                "form": form,
                "error": "email or password is incorrect",
            }
            return render(request, "customer/login.html", ctx)
    elif request.method == "GET":
        form = LoginForm()
        ctx = {
            "form": form,
        }
        return render(request, "customer/login.html", ctx)

def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return redirect("Customer:customer_home")
    elif request.method == "GET":
        return render(request, "customer/logout.html")

def customer_home(request):
    return PageMaker.get_page(request, template_name="customer/customer_home.html")

#Show All List
#Show All List
@login_required
def customer_confirm(request):
    picture_request = DBConnector.get_request_all(request)
    context = {
        'picture_request' : picture_request,
        'request_user' : request.user
    }
    if(picture_request):
        AlarmOperator.activate(request, "요청이 있습니다.")
    return PageMaker.get_page(request, "customer/customer_confirm.html", context)

#READ
def customer_read(request, pk):
    picture_request = get_object_or_404(PictureRequest, pk=pk)
    document = picture_request.document
    context= {
        'picture_request' : picture_request,
        'document' : document
    }
    return PageMaker.get_page(request, template_name="customer/customer_read.html", context=context)


def picture_upload(request, pk):
    picture_request = get_object_or_404(PictureRequest, pk=pk)
    clerk = picture_request.clerk
    customer = request.user
    if request.method == 'POST':
        form = PictureRequestForm(request.POST, request.FILES, instance=picture_request)
        if form.is_valid():
            picture_request.clerk = clerk
            picture_request.customer = customer
            picture_request.uploaded = True
            picture_request = form.save()
            picture_request.image = request.FILES.get('image')

            return redirect('PictureHandler:picture_handler_encryptor', pk)
    else:
        form = PictureRequestForm(instance=picture_request)
    return PageMaker.get_page(request, template_name="Customer/picture_upload.html", context = {'form': form, 'pk':pk, 'clerk':clerk, 'customer':customer })