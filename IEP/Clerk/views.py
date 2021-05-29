from django.forms import fields
from django.shortcuts import  redirect
from core.models import *
from core.forms import *
from .forms import *
from .models import *
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .utils import *
from django.shortcuts import render, get_object_or_404, redirect


def clerk_home(request):
    return Page_maker.make_page(request, "clerk/clerk_home.html")


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_clerk = True
            user.save()
            return redirect("Clerk:clerk_home")
        else:
            ctx = {
                "form": form,
            }
            return Page_maker.make_page(request, "clerk/sign_up.html", ctx)

    elif request.method == "GET":
        form = SignUpForm()
        ctx = {
            "form": form,
        }
        return Page_maker.make_page(request, "clerk/sign_up.html", ctx)

def login(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None and user.is_clerk == True:
            auth_login(request, user)

            return redirect("Clerk:clerk_home")
        else:
            ctx = {
                "form": form,
                "error": "Check your email or password is incorrect",
            }
            return Page_maker.make_page(request, "clerk/login.html", ctx)
    elif request.method == "GET":
        form = LoginForm()
        ctx = {
            "form": form,
        }
        return Page_maker.make_page(request, "clerk/login.html", ctx)

 
def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return redirect("Clerk:clerk_home")
    elif request.method == "GET":
        
        return Page_maker.make_page(request, "clerk/logout.html")

@login_required
def select_customer(request):
    if request.method == "POST":
        form = FindCustomerForm(request.POST)
        if Customer_checker.compare(form):
            return redirect('select/{0}'.format(form.cleaned_data['customer_name']))
        else:
            Notification_operator.notify(request,"존재하지 않는 고객입니다.")

            return redirect('Clerk:clerk_home')
    else:
        form = FindCustomerForm()
        return Page_maker.make_page(request, "clerk/select_customer.html", {"form": form})


#Create
@login_required
def picture_request_create(request):
    user = request.user
    if request.method == "POST":
        form = PictureRequestForm(request.POST)
        if form.is_valid():
            picture = form.save()
            picture.clerk = user
            picture = form.save()
            return redirect('Customer:customer_home')
    else:
        form = PictureRequestForm()
        return render(request, "clerk/picture_request_create.html", {"form": form})


def picture_request_list(request):
    picture_request = PictureRequest.objects.filter(clerk=request.user)
    context = {
        "picture_request": picture_request,
    }
    print("already packed")
    return render(request, "clerk/picture_request_list.html", context)


def picture_download(request, pk):
    picture_request = get_object_or_404(PictureRequest, pk=pk)
    context = {
        "picture_request": picture_request
    }
    return render(request, "clerk/picture_download.html", context)

def picture_decryptor(request, pk):
    return redirect("PictureHandler:picture_handler_decryptor", pk)



class select_document_view(View):
    def get(self, request, customer_name):

        documents = DB_connector.get_document_list()
        customer = User.objects.get(username__exact=customer_name)
        
        return Page_maker.make_page(request,"clerk/select_document.html",{"customer": customer, "documents": documents})

    def post(self, request, customer_name): 
        user = request.user
        form = PictureRequestForm(request.POST)

        if request.POST['document'] == '':
            print(request.POST)

            documents = DB_connector.get_document_list()
            customer = User.objects.get(username__exact=customer_name)

            Notification_operator.notify(request,"문서를 확인해주세요.")

            return Page_maker.make_page(request,"clerk/select_document.html",{"customer": customer, "documents": documents})

        DB_connector.create(form, user)
        Notification_operator.notify(request,"요청생성이 완료되었습니다.")

        return redirect('Clerk:clerk_home')
