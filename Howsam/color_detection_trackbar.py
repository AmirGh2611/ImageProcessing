import cv2
import numpy as np


def nothing(x):
    pass


# Load image
img = cv2.imread("Data/flowers.jpg")
if img is None:
    print("Error: Could not load image")
    exit()

cv2.namedWindow("image")
cv2.createTrackbar("H_low", "image", 0, 179, nothing)
cv2.createTrackbar("S_low", "image", 0, 255, nothing)
cv2.createTrackbar("V_low", "image", 0, 255, nothing)
cv2.createTrackbar("H_up", "image", 179, 179, nothing)
cv2.createTrackbar("S_up", "image", 255, 255, nothing)
cv2.createTrackbar("V_up", "image", 255, 255, nothing)

while True:
    h_low = cv2.getTrackbarPos("H_low", "image")
    s_low = cv2.getTrackbarPos("S_low", "image")
    v_low = cv2.getTrackbarPos("V_low", "image")
    h_up = cv2.getTrackbarPos("H_up", "image")
    s_up = cv2.getTrackbarPos("S_up", "image")
    v_up = cv2.getTrackbarPos("V_up", "image")

    # Convert to HSV (standard range: H:0-179, S:0-255, V:0-255)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([h_low, s_low, v_low])
    upper = np.array([h_up, s_up, v_up])
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("image", result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()