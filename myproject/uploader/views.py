from django.shortcuts import render, redirect

from .forms import VideoUploadForm
from video.models import Video


def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_videos = request.FILES.getlist('video')
            for video in uploaded_videos:
                obj = Video.objects.create(video=video)
                obj.save()
                # TODO celery start task
            return redirect('video:videos_list')
    else:
        form = VideoUploadForm()
    return render(request, 'video_upload/upload_video.html', {'form': form})
