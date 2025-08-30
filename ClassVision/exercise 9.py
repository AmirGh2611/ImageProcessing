import cv2
import numpy as np

img_gray = cv2.imread("Data/numbers.jpg", 0)
blur = cv2.GaussianBlur(img_gray, (9, 9), 0)
bin_img = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

kernel = np.ones((3, 3), np.uint8)
mask = cv2.morphologyEx(bin_img, cv2.MORPH_CLOSE, kernel, iterations=1)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN,  kernel, iterations=1)

num, labels, stats, _ = cv2.connectedComponentsWithStats(mask, connectivity=8)
areas = stats[1:, cv2.CC_STAT_AREA]
min_area = img_gray.shape[0] * img_gray.shape[1] * 0.001
count = int((areas >= min_area).sum())
print(count)

cv2.imshow("mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
