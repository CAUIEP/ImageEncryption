from django import forms
from core.models import *


class FindCustomerForm(forms.Form):
    customer_name = forms.CharField(label='Customer name', max_length=30)