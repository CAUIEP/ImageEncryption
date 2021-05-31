from collections import UserDict
from django import forms
from django.forms import widgets
from core.models import *
from .models import *
from django.contrib.auth.forms import UserCreationForm



class FindCustomerForm(forms.Form):
    customer_name = forms.CharField(label='Customer name', max_length=30)

class RequestForm(forms.ModelForm):
    class Meta:
        model = PictureRequest
        fields = ['customer','document']
        DOC_CHOICES  = (
            ('','------------'),
            ('주민등록등본', '주민등록등본'),
            ('통장사본', '통장사본'),
            ('가족관계증명서', '가족관계증명서'),
            ('신분증사본', '신분증사본')
        )
        widgets={
            'document' : forms.Select(choices=DOC_CHOICES,attrs={'id':'docSelect'}),
        }

class ClerkSignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_update_fields = ['password1', 'password2']
        for field_name in class_update_fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'clerkSignupForm'
            })
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'clerkSignupForm'}),
            'email': forms.EmailInput(attrs={'class': 'clerkSignupForm'}),
        }