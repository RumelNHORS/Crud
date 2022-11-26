from django.contrib import admin
from . models import User

@admin.register(User)
class UserAdminClass(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject', 'email', 'password']
