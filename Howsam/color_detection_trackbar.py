import cv2
import numpy as np


def read_video(cam):
    cap = cv2.VideoCapture(cam)
    if cap.isOpened():
        while True:
            ret, frame = cap.read()
            if ret:
                color_thresholding(frame)
            else:
                print("frame lost!")
                cap.release()
                break
    else:
        print("Unable to open camera!")
        cap.release()


def image_read(url):
    img = cv2.imread(url)
    color_thresholding(img)


def color_thresholding(image_bgr, h_low=None, s_low=None, v_low=None, h_up=None, s_up=None, v_up=None):
    image_bgr_norm = cv2.normalize(image_bgr, None, 0, 1, cv2.NORM_MINMAX, dtype=cv2.CV_32FC3)
    image_hsv = cv2.cvtColor(image_bgr_norm, cv2.COLOR_BGR2HSV)
    lower_bound = np.array([h_low, s_low, v_low], dtype="float32")
    higher_bound = np.array([h_up, s_up, v_up], dtype="float32")
    mask = cv2.inRange(image_hsv, lower_bound, higher_bound)
    result = cv2.bitwise_and(image_bgr, image_bgr, mask=mask)


image_read("Data/flowers.jpg")
cv2.destroyAllWindows()
