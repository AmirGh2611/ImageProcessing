import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Data/lenna forsen.png', 0)
result = []
for i in range(256):
    a = np.where(img == i, 1, 0)
    a = a / img.size
    result.append(a.sum())
plt.plot(range(256), result)
plt.show()
