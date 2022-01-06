from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    ...
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("cerbere_uid",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("cerbere_uid",)}),)


admin.site.register(User, CustomUserAdmin)
