from django.contrib import admin
from username.models import Username

@admin.register(Username)
class UserNameAdmin(admin.ModelAdmin):
    pass