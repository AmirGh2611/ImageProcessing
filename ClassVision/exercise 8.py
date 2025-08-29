import cv2

img = cv2.imread('Data/numbers.jpg', cv2.IMREAD_GRAYSCALE)
blur = cv2.GaussianBlur(img, (9, 9), 0)
result = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow('image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
