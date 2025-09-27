import cv2
import numpy as np


def ball_finder(image_bgr):
    img_bgr_norm = cv2.normalize(image_bgr, None, 0, 1, cv2.NORM_MINMAX, dtype=cv2.CV_32FC3)
    img_hsv = cv2.cvtColor(img_bgr_norm, cv2.COLOR_BGR2HSV)
    lower_bound = np.array([60, 0, 0], dtype="float32")
    upper_bound = np.array([170, 0.8, 0.8], dtype="float32")
    mask = cv2.inRange(img_hsv, lower_bound, upper_bound)
    result = image_bgr.copy()
    result[mask == 255] = [0, 0, 255]
    return result


cap = cv2.VideoCapture("Data/tennis.mp4")
if cap.isOpened():
    while True:
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (450, 600))
            ball = ball_finder(frame)
            cv2.imshow("result", ball)
            if cv2.waitKey(20) == ord("q"):
                break
        else:
            print("frame not found!")
            break
else:
    print("video not found!")
cap.release()
cv2.destroyAllWindows()
