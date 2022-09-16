from rest_framework.routers import DefaultRouter
from username.api.views import UserNameViewSet

router_username = DefaultRouter()

router_username.register(prefix='username', basename='username', viewset=UserNameViewSet)