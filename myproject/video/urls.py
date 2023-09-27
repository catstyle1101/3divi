from django.urls import path

from video import views

app_name = 'video'

urlpatterns = [
    path('', views.video_list, name='videos_list'),
    path('tasks/<task_id>/revoke', views.revoke_task, name='revoke_task'),
    path('tasks/<task_id>/pause', views.pause_task, name='pause_task'),
    path('tasks/<task_id>/unpause', views.unpause_task, name='unpause_task'),
]
