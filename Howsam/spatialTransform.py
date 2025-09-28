import cv2
import numpy as np

img = cv2.imread("Data/book-3.bmp")
source_dots = np.array([[278, 135],
                        [488, 211],
                        [22, 398],
                        [289, 578]], dtype="float32")
h, w = img.shape[:2]
target_dots = np.array([[0, 0],
                        [w - 1, 0],
                        [0, h - 1],
                        [w - 1, h - 1]], dtype="float32")
perspective_matrix = cv2.getPerspectiveTransform(source_dots, target_dots)
warped = cv2.warpPerspective(img, perspective_matrix, (w, h), flags=cv2.INTER_LANCZOS4)
cv2.imshow("Original", img)
cv2.imshow("Warped", warped)
cv2.waitKey(0)
cv2.destroyAllWindows()
