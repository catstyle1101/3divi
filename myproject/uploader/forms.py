from django import forms
from django.conf import settings

from multiupload.fields import MultiMediaField

from video.models import Video


class VideoUploadForm(forms.ModelForm):
    video = MultiMediaField(
        min_num=1, max_num=5, max_file_size=1024*1024*100, media_type='video')

    class Meta:
        model = Video
        fields = [
            'video',
        ]

    def save(self, commit=True):
        instance = super(VideoUploadForm, self).save(commit)
        for each in self.cleaned_data['files']:
            Video.objects.create(file=each, message=instance)

        return instance

    def clean(self):
        videos = self.cleaned_data['video']
        for data in videos:
            if data.name.split('.')[-1] not in settings.VIDEO_FILETYPES:
                message = (
                    'Формат видео должен быть: ' + ', '.join(
                        settings.VIDEO_FILETYPES))
                self.add_error('video', message)
