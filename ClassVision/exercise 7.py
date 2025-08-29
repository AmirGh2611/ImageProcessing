import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (350, 350))
        img_gamma_correction1_2 = np.clip(pow(frame / 255.0, (1 / 2)) * 255.0, 0, 255).astype(np.uint8)
        img_gamma_correction1_4 = np.clip(pow(frame / 255.0, (1 / 4)) * 255.0, 0, 255).astype(np.uint8)
        img_gamma_correction2 = np.clip(pow(frame / 255.0, 2) * 255.0, 0, 255).astype(np.uint8)
        img_gamma_correction4 = np.clip(pow(frame / 255.0, 4) * 255.0, 0, 255).astype(np.uint8)
        cv2.imshow("gamma correction 1/2", img_gamma_correction1_2)
        cv2.imshow("gamma correction 1/4", img_gamma_correction1_4)
        cv2.imshow("gamma correction 2", img_gamma_correction2)
        cv2.imshow("gamma correction 4", img_gamma_correction4)
        cv2.imshow('original', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        print("error in webcam")
cap.release()
cv2.destroyAllWindows()
