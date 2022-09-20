from rest_framework.routers import DefaultRouter
from data.api.views import DataViewSet

router_data = DefaultRouter()
router_data.register(prefix='data', basename='data', viewset=DataViewSet)