from django.contrib import admin
from messagesText.models import Messages

@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    pass

