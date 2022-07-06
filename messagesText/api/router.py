from rest_framework.routers import DefaultRouter
from messagesText.api.views import MessagesTextViewSet

router_message = DefaultRouter()

router_message.register(prefix='message', basename='message', viewset=MessagesTextViewSet)