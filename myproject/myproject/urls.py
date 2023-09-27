from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title='3divi test case',
        default_version='v1',
        description='API for test case 3divi',
        license=openapi.License(name='MIT License'),
    ),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', include('uploader.urls'), name='uploader'),
    path('api/v1/', include('api.urls'), name='api'),
    path(
        'api/docs/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='swagger-ui',
    ),
    path('', include('video.urls'), name='video'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
