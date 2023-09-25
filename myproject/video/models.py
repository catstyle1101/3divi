from django.db import models
from django.utils.translation import gettext_lazy as _

from video.mixins import UpdateMixin


class Video(models.Model, UpdateMixin):
    class Status(models.TextChoices):
        IN_PROGRESS = 'in_progress', _('IN PROGRESS')
        PAUSED = 'paused', _('PAUSED')
        CANCELED = 'canceled', _('CANCELLED')
        FINISHED = 'finished', _('FINISHED')

    video = models.FileField('Видео', upload_to='videos/')
    progress = models.SmallIntegerField('Прогресс', default=0)
    status = models.CharField(
        'Статус',
        choices=Status.choices,
        default=Status.IN_PROGRESS,
        max_length=20
    )
    count_faces = models.SmallIntegerField(
        'Количество уникальных лиц на видео',
        default=0,
    )

    def __str__(self):
        return self.video.name.split('/')[-1]
