from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username']
    list_display_links = ['email', 'username']

@admin.register(PictureRequest)
class PictureRequestAdmin(admin.ModelAdmin):
    list_display = ['clerk', 'customer']
    list_display_links = ['clerk', 'customer']