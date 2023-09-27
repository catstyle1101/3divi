from django.shortcuts import render, redirect

from .models import Video
from myproject import celery_app as app


def video_list(request):
    videos = Video.objects.all()
    return render(
        request,
        'video/videos/list.html',
        {
            'videos': videos,
            'Video': Video,
            'stopped_statuses': [
                Video.Status.CANCELED,
                Video.Status.PAUSED,
                Video.Status.FINISHED,
            ],
        }
    )


def revoke_task(request, task_id):
    video = Video.objects.get(task_id=task_id)
    video.update(status=Video.Status.CANCELED)
    return redirect('video:videos_list')
