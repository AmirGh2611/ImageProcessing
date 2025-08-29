import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Data/woman.jpg")

img_gamma_correction1_6 = np.clip(pow(img / 255.0, (1 / 6)) * 255.0, 0, 255).astype(np.uint8)
img_gamma_correction1_5 = np.clip(pow(img / 255.0, (1 / 5)) * 255.0, 0, 255).astype(np.uint8)
img_gamma_correction1_4 = np.clip(pow(img / 255.0, (1 / 4)) * 255.0, 0, 255).astype(np.uint8)
img_gamma_correction1_3 = np.clip(pow(img / 255.0, (1 / 3)) * 255.0, 0, 255).astype(np.uint8)
img_gamma_correction1_2 = np.clip(pow(img / 255.0, (1 / 2)) * 255.0, 0, 255).astype(np.uint8)

img_linear_correction_10 = cv2.add(img, 10)
img_linear_correction_30 = cv2.add(img, 30)
img_linear_correction_50 = cv2.add(img, 50)
img_linear_correction_70 = cv2.add(img, 70)
img_linear_correction_90 = cv2.add(img, 90)

plt.figure(figsize=(12, 8))
plt.subplot(251);plt.imshow(img_gamma_correction1_2, cmap='gray'), plt.title('g=1/2')
plt.subplot(252);plt.imshow(img_gamma_correction1_3, cmap='gray'), plt.title('g=1/3')
plt.subplot(253);plt.imshow(img_gamma_correction1_4, cmap='gray'), plt.title('g=1/4')
plt.subplot(254);plt.imshow(img_gamma_correction1_5, cmap='gray'), plt.title('g=1/5')
plt.subplot(255);plt.imshow(img_gamma_correction1_6, cmap='gray'), plt.title('g=1/6')

plt.subplot(256);plt.imshow(img_linear_correction_10, cmap='gray'), plt.title('L=10')
plt.subplot(257);plt.imshow(img_linear_correction_30, cmap='gray'), plt.title('L=30')
plt.subplot(258);plt.imshow(img_linear_correction_50, cmap='gray'), plt.title('L=50')
plt.subplot(259);plt.imshow(img_linear_correction_70, cmap='gray'), plt.title('L=70')
plt.subplot(2, 5, 10);plt.imshow(img_linear_correction_90, cmap='gray'), plt.title('L=90')
plt.show()
