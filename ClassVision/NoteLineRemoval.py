import cv2

img = cv2.imread("Data/note.png", 0)
img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
img = cv2.bitwise_not(img)
length = img.shape[1] // 10
HorizontalStruc = cv2.getStructuringElement(cv2.MORPH_RECT, (length, 1))
horizontal = cv2.morphologyEx(img, cv2.MORPH_OPEN, HorizontalStruc)
cv2.imshow('horizontal', horizontal)
cv2.waitKey(0)
cv2.destroyAllWindows()
