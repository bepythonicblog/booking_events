from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from authentication.models import User

class UserAdmin(BaseUserAdmin):
    list_display = ('username','email','first_name','last_name')


admin.site.register(User,UserAdmin)