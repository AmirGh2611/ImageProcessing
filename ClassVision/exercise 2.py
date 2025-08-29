import cv2
import numpy as np

img = cv2.imread("Data/AdamDriver.png")
imgWithAlpha = np.ones((img.shape[0], img.shape[1], 4))*127
imgWithAlpha[..., 0:3] = img
imgWithAlpha[180:500, 400:650, 3] = 255
cv2.imwrite("Data/Transparency.png", imgWithAlpha)
