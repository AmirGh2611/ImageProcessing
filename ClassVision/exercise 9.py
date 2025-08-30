import cv2
import numpy as np

img = cv2.imread('Data/numbers.jpg', 0)
blur = cv2.GaussianBlur(img, (9, 9), 0)
result = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
kernel = np.ones((2, 2), np.uint8)
closing = cv2.morphologyEx(result, cv2.MORPH_CLOSE, kernel)
num_labels, labels = cv2.connectedComponents(closing)
label_hue = np.uint8(179 * labels / np.max(labels))
blank = np.ones_like(img) * 255
labeled_img = cv2.merge([label_hue, blank, blank])
labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)
labeled_img[label_hue == 0] = 0
cv2.imshow('image', labeled_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
