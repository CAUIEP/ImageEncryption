from django.shortcuts import render
from core.models import *
from core.forms import *
from django.contrib import messages

class DB_connector:

    @classmethod
    def get_customer_list(cls):
        customers = User.objects.all()
        return customers

    @classmethod
    def get_document_list(cls):
        documents = Document.objects.all()
        return documents

    @classmethod
    def create(cls, form,user):
        if form.is_valid():
            picture = form.save()
            picture.clerk = user
            picture = form.save()

class Customer_checker:
    customers = DB_connector.get_customer_list()

    @classmethod
    def compare(cls, customer_info):
        if customer_info.is_valid():
            customer_name = customer_info.cleaned_data['customer_name']
            for customer in cls.customers:
                if customer.username == customer_name and customer.is_customer == 1:  # check customer
                    return True
            return False

class Page_maker:

    @classmethod
    def make_page(cls, request, html, *ctx):
        if len(ctx)!=0:
            return render(request, html, ctx[0])
        
        return render(request, html)

class Notification_operator:
    
    @classmethod
    def notify(cls,request,msg):
        messages.info(request,msg)

