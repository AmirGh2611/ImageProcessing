import cv2
import numpy as np

img = cv2.imread("Data/AdamDriver.png")
img_gray = np.zeros(img.shape[:2], dtype=np.float32)
img_gray = img[..., 0]*0.1140 + img[..., 1]*0.5870 + img[..., 2]*0.2989
img_gray = img_gray.astype(np.uint8)
cv2.imshow("Adam Driver Image", img_gray)
cv2.waitKey()
cv2.destroyAllWindows()
