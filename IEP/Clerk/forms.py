from django import forms
from core.models import *
from .models import *


class FindCustomerForm(forms.Form):
    customer_name = forms.CharField(label='Customer name', max_length=30)

class PictureRequestForm(forms.ModelForm):
    class Meta:
        model = PictureRequest
        fields = ['customer','document']