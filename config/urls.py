from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Authorization Service API",
        default_version='v1',
        description="Проект представляет собой реализацию простой реферальной системы. "
                    "Основной функционал включает авторизацию пользователей по номеру "
                    "телефона и возможность использования инвайт-кодов.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="artkamproject@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('elect_shop.urls')),
    path('users/', include('users.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]