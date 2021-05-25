from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from core.models import User
from core.forms import *
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required


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
    return render(request, "customer/customer_home.html")

# Create your views here.
