import cv2
import numpy as np

# Read image
img = cv2.imread("Data/sign.jpg")
img = cv2.resize(img, (1000, 600))

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur for denoising
blur = cv2.GaussianBlur(gray, (9, 9), 0)

# Threshold (signature = white, background = black)
thresh = cv2.adaptiveThreshold(
    blur, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV,
    11, 2
)

# Create RGBA image
b, g, r = cv2.split(img)
alpha = thresh  # signature = 255, background = 0
rgba = cv2.merge([b, g, r, alpha])

cv2.imshow("Signature Transparent", rgba)
cv2.waitKey(0)
cv2.destroyAllWindows()
