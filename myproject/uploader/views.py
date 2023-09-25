from django.shortcuts import render, redirect

from .forms import VideoUploadForm
from .models import Video


def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_videos = request.FILES.getlist('video')
            for video in uploaded_videos:
                obj = Video.objects.create(video=video)
                obj.save()
                # TODO celery start task
            return redirect('uploader:upload_video')
    else:
        form = VideoUploadForm()
    return render(request, 'video_upload/upload_video.html', {'form': form})


def video_list(request):
    videos = Video.objects.all()
    return render(
        request,
        'videos/list.html',
        {
            'videos': videos,
            'Video': Video,
        }
    )
