import cv2
import face_recognition

# https://github.com/mayankjn34/unique-faces-count-in-video/blob/master/Unique_faces_identify_video.py

input_movie = cv2.VideoCapture("sample_1.mp4")
length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))
# output_movie = cv2.VideoWriter("output_faces_final.avi",cv2.VideoWriter_fourcc(*'DIVX'), 24, (640,360))


# Initialize variables
face_locations = []
face_encodings = []
face_names = []
frame_number = 0
res = 0
known_faces = []
while True:
    # Grab a single frame of video
    ret, frame = input_movie.read()
    frame_number += 1

    # Quit when the input video file ends
    if not ret:
        break

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame, model="hog")
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding in face_encodings:
        if frame_number == 1:
            #finding first frame and using faces as stating base line
            known_faces.append(face_encoding)
            res += 1
        else:
            # See if the face is a match for the known face(s)
            match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.65)
            y = False
            for i in match:
                #if faces already identified then do not count it
                if i:
                    y = True
                    break
            if y:
                continue
            else :
                #counting unique faces
                known_faces.append(face_encoding)
                res += 1
    # font = cv2.FONT_HERSHEY_DUPLEX
    #counting display
    # cv2.putText(frame, "Count = "+str(res), (400, 50), font, 0.5, (255, 255, 255), 1)
    print("Writing frame {} / {}".format(frame_number, length))
    #writing frames to other video
    # output_movie.write(frame)

# All done!
print(res)
input_movie.release()
cv2.destroyAllWindows()
