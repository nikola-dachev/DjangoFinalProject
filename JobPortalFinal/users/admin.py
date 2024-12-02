from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from JobPortalFinal.users.models import CustomUser


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email', 'first_name', 'last_name',)
    search_fields = ('pk', 'username', 'email', 'first_name', 'last_name')
    ordering = ('-pk',)
    list_filter = ('email', 'first_name', 'last_name')
