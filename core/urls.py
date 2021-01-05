from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from apps.test_one.views import home
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="FCApp ver 2 API",
        default_version='v1',
        description="FCApp API new version",
        terms_of_service="we use ur data, deal with it",
        contact=openapi.Contact(email="contact@akanza.pl"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', home, name='test')
]
