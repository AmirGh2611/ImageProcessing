import cv2
import numpy as np

img = np.zeros((500, 500), "uint8")
start = (1 / 3) * (img.shape[1])
stop = (2 / 3) * (img.shape[1])
cv2.rectangle(img, (int(start), 300), (int(stop), 500), (255, 255, 255), 2)
cv2.line(img, (int(start), 300), (int(start + 80), 150), (255, 255, 255), 2)
cv2.line(img, (int(start + 80), 150), (int(stop), 300), (255, 255, 255), 2)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("Data/drawing.jpg", img)
