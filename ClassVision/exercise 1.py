import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Data/AdamDriver.png')
crop = img[180:500, 400:650]
plt.imshow(img[..., ::-1])
plt.imshow(crop[..., ::-1])
plt.show()
cv2.imwrite('Data/AdamDriver_face.jpg', crop)