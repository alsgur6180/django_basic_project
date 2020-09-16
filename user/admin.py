from django.contrib import admin
from .models import UserInfo


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')


admin.site.register(UserInfo, UserAdmin)
