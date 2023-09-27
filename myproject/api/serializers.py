from rest_framework import serializers

from video.models import Video


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ('id', 'video', 'status', 'progress', 'task_id')
        read_only_fields = ('status', 'progress', 'task_id')
