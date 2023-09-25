from mtcnn import MTCNN
import cv2


videopath = "sample.mp4"


def detect_faces(videopath: str, show_frames: bool = False):
    detector = MTCNN()
    cap = cv2.VideoCapture(videopath)
    fps = int(cap.get(5))
    frame_count = cap.get(7)
    idx = 0
    count_faces_in_frame = dict()
    while cap.isOpened():
        ret, frame = cap.read()
        if ret is True:
            while show_frames:
                cv2.imshow('Look', frame)
                if cv2.waitKey(1) == ord("q"):
                    break
            result = detector.detect_faces(frame)
            count_faces_in_frame[idx] = len(
                [i for i in result if i['confidence'] >= 0.9])
            idx += 1
    return result


if __name__ == '__main__':
    detect_faces(videopath=videopath, show_frames=True)
