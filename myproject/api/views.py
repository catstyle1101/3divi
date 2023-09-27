from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from face_finder.tasks import find_faces
from video.models import Video
from .serializers import VideoSerializer


class VideoListView(ListModelMixin, CreateModelMixin, GenericViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    parser_classes = (MultiPartParser,)

    @action(methods=['GET'], detail=True)
    def pause(self, request, *args, **kwargs):
        """
        Set face recognition on pause.

        -----
        """
        video = Video.objects.filter(pk=kwargs.get('pk'))
        if video.exists():
            video[0].update(status=Video.Status.PAUSED)
        return Response({'paused': True})

    @action(methods=['GET'], detail=True)
    def unpause(self, request, *args, **kwargs):
        """
        Unpause face recognition by video_id.

        -----
        """
        video = Video.objects.filter(pk=kwargs.get('pk'))
        if video.exists():
            video[0].update(status=Video.Status.IN_PROGRESS)
        return Response({'paused': False})

    @action(methods=['GET'], detail=True)
    def revoke(self, request, *args, **kwargs):
        """
        Revoke face recognition.

        -----
        """
        video = Video.objects.filter(pk=kwargs.get('pk'))
        if video.exists():
            video[0].update(status=Video.Status.CANCELED)
        return Response({'revoked': True})

    def create(self, request, *args, **kwargs):
        """
        Upload video and set to face recognition task.

        -----
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        find_faces.delay(serializer.instance.id)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        """
        Show all Videos list.

        -----
        """
        return super().list(request, *args, **kwargs)
