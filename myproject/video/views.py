from django.shortcuts import render, redirect

from .models import Video


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
    video = Video.objects.filter(task_id=task_id)
    if video.exists():
        video[0].update(status=Video.Status.CANCELED)
    return redirect('video:videos_list')


def pause_task(request, task_id):
    video = Video.objects.filter(task_id=task_id)
    if video.exists():
        video[0].update(status=Video.Status.PAUSED)
    return redirect('video:videos_list')


def unpause_task(request, task_id):
    video = Video.objects.filter(task_id=task_id)
    if video.exists():
        video[0].update(status=Video.Status.IN_PROGRESS)
    return redirect('video:videos_list')
