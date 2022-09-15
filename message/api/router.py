from rest_framework.routers import DefaultRouter
from message.api.views import MessagesViewSet

router_message = DefaultRouter()
router_message.register(prefix='message', basename='message', viewset=MessagesViewSet)