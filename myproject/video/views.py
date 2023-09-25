from django.shortcuts import render

from .models import Video


def video_list(request):
    videos = Video.objects.all()
    return render(
        request,
        'video/videos/list.html',
        {
            'videos': videos,
            'Video': Video,
        }
    )
