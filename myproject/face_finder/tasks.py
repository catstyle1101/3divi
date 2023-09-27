import logging

from celery import shared_task, current_task
import cv2
from django.conf import settings
import face_recognition
import numpy

from video.models import Video


@shared_task(bind=True)
def find_faces(self, pk: int) -> None:
    """
    Get instance of Video model. Search unique faces and update instance.
    """
    max_retry = 20
    video = Video.objects.get(pk=pk)
    video.update(task_id=current_task.request.id)
    video_length = retries = 0
    while video_length == 0 and retries < max_retry:
        input_movie = cv2.VideoCapture(video.video.path)
        video_length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))
        retries += 1
    if video_length == 0:
        logging.error('Video cannot be analyze')
        return

    logging.info(f'Video {video.video.path} length is {video_length}')

    face_locations = []
    face_encodings = []
    frame_number = 0
    count_unique_faces = 0
    known_faces = []
    progress_percent = 0
    while True:
        video.update(status=Video.Status.IN_PROGRESS)
        ret, frame = input_movie.read()
        frame_number += 1
        if not ret:
            break
        rgb_frame = numpy.ascontiguousarray(frame[:, :, ::-1])

        face_locations = face_recognition.face_locations(
            rgb_frame, model="hog")
        face_encodings = face_recognition.face_encodings(
            rgb_frame, face_locations)

        for face_encoding in face_encodings:
            if frame_number == 1:
                known_faces.append(face_encoding)
                count_unique_faces += 1
            else:
                match = face_recognition.compare_faces(
                    known_faces,
                    face_encoding,
                    tolerance=settings.FACE_COMPARE_TOLERANCE,
                )
                y = False
                for i in match:
                    if i:
                        y = True
                        break
                if y:
                    continue
                else:
                    known_faces.append(face_encoding)
                    count_unique_faces += 1
        percent = int(frame_number//(video_length/100))
        if percent > progress_percent:
            progress_percent = percent
            logging.info(f'{video.video} processing {progress_percent}%')
            video.update(
                progress=progress_percent, count_faces=count_unique_faces)

    input_movie.release()
    cv2.destroyAllWindows()
    video.update(status=Video.Status.FINISHED, progress=progress_percent)
    logging.info(f'{video.video} processing finished')
