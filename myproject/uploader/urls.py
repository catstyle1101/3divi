from django.urls import path

from uploader import views

app_name = 'uploader'

urlpatterns = [
    path('', views.upload_video, name='upload_video'),
    path('videos', views.video_list, name='videos_list'),
]
