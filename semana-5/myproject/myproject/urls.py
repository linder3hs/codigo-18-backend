from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title='Django API G18',
        default_version='v1',
        description='API Codigo G18',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email='linder@gmail.com'),
        license=openapi.License(name="MIT")
    ),
    public=True,
    permission_classes=(AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('storeapp.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='swagger-api')
]
