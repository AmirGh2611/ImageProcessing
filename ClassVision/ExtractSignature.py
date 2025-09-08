import cv2
import numpy as np

# Read image
img = cv2.imread("Data/sign.jpg")
img = cv2.resize(img, (1000, 600))

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Denoise a bit
blur = cv2.GaussianBlur(gray, (9, 9), 0)

# Threshold (invert so signature = white, background = black)
thresh = cv2.adaptiveThreshold(
    blur, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV,
    11, 2
)

# Create mask where signature is white
mask = thresh

# Convert single channel mask to 3 channels
mask_3 = cv2.merge([mask, mask, mask])

# Apply mask to original image
result = cv2.bitwise_and(img, mask_3)

# Optional: make background white instead of black
white_bg = np.full_like(img, 255)
final = np.where(mask_3 == 0, white_bg, result)


cv2.imshow("Signature Extracted", final)
cv2.waitKey(0)
cv2.destroyAllWindows()
