"""Haarcascade image example"""
import cv2 as cv
import imageio

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")


def detect(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for x, y, w, h in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        roi_gray = gray[y : y + h, w : x + w]
        roi_color = frame[y : y + h, w : x + w]
    return frame


image = imageio.imread("faces.jpg")
image = detect(image)
cv.imshow("image", image)
if cv.waitKey():
    imageio.imwrite("output.jpg", image)
    exit()
