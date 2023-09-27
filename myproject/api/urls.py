from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api import views

app_name = 'api'


router = SimpleRouter()

router.register('video', views.VideoListView, basename='video')


urlpatterns = [
    path('', include(router.urls)),
]
