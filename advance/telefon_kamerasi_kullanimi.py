"""Telefon Kamera Kullanımı."""
import cv2
# import numpy as np

url = "192.168.1.1"
cap = cv2.VideoCapture()
while True:
    camera, frame = cap.read()
    if frame is not None:
        cv2.imshow("Frame", frame)
    q = cv2.waitKey(1)
    if q == ord("q"):
        break
cv2.destroyAllWindows()
