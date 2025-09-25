import cv2
import numpy as np

img = cv2.imread('Data/flowers.jpg')
img = cv2.normalize(img, None, 0, 1, cv2.NORM_MINMAX, dtype=cv2.CV_32FC3)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_red1 = np.array([0, 0.3, 0.4], dtype="float32")
upper_red1 = np.array([20, 1, 1], dtype="float32")

lower_red2 = np.array([350, 0.3, 0.4], dtype="float32")
upper_red2 = np.array([360, 1, 1], dtype="float32")
# create mask
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2)
# putting mask on image
res = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('original', img)
cv2.imshow('result', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
