from django.contrib import admin
from message.models import Messages

@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    pass
