import cv2
import face_recognition
import numpy
from celery import shared_task
from django.conf import settings

from video.models import Video



input_movie = cv2.VideoCapture("faces.mp4")
length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))

face_locations = []
face_encodings = []
frame_number = 0
count_unique_faces = 0
known_faces = []
while True:
    ret, frame = input_movie.read()
    frame_number += 1
    if not ret:
        break
    rgb_frame = numpy.ascontiguousarray(frame[:, :, ::-1])

    face_locations = face_recognition.face_locations(rgb_frame, model="hog")
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding in face_encodings:
        if frame_number == 1:
            known_faces.append(face_encoding)
            count_unique_faces += 1
        else:
            match = face_recognition.compare_faces(
                known_faces, face_encoding, tolerance=0.65)
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
    font = cv2.FONT_HERSHEY_DUPLEX
    print(f"{int(frame_number//(length/100))} %")

input_movie.release()
cv2.destroyAllWindows()
