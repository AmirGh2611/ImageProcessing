import cv2
import numpy as np

cap = cv2.VideoCapture("Data/road_video.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    frame_norm = cv2.normalize(frame, None, 0, 1, cv2.NORM_MINMAX, dtype=cv2.CV_32FC3)

    hsv = cv2.cvtColor(frame_norm, cv2.COLOR_BGR2HSV)
    lower_red1 = np.array([0, 0.3, 0.2], dtype="float32")
    upper_red1 = np.array([20, 1, 1], dtype="float32")

    lower_red2 = np.array([330, 0.3, 0.2], dtype="float32")
    upper_red2 = np.array([360, 1, 1], dtype="float32")
    # create mask
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)
    # putting mask on image
    res = cv2.bitwise_and(frame_norm, frame_norm, mask=mask)
    cv2.imshow('original', frame)
    cv2.imshow('result', res)
    if cv2.waitKey(20) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
