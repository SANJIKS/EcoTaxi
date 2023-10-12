from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="ECO TAXI",
        default_version='v1',
        description="API for Evion",
        terms_of_service="https://evion.kg",
        contact=openapi.Contact(email="evionteam1@gmail.com"),
        license=openapi.License(name="Evion"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('user/', include('djoser.urls')),
    path('login/', include('djoser.urls.jwt')),
    path('', include('apps.users.urls')),
    path('drivers/', include('apps.drivers.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)