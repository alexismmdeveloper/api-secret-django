from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from username.api.router import router_username
from message.api.router import router_message

schema_view = get_schema_view(
   openapi.Info(
      title="SECRET API",
      default_version='v1',
      description="Api secret",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include(router_username.urls)),
    path('api/', include(router_message.urls))
]
