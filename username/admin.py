from django.contrib import admin
from username.models import Username

@admin.register(Username)
class UsernameAdmin(admin.ModelAdmin):
    list_display = ['id','username']
