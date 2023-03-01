import cv2  # pip install opencv-python
# https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml




# def yuz_algilama(img):
#     # img = cv2.imread('image.jpg')
#     yuzler = yuz_cehresi.detectMultiScale(img, 1.1, 4)

#     for (x, y, w, h) in yuzler:
#         cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
#     cv2.imwrite('face_detected.png', img)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    frame = img.copy()
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow("Face Detected", frame)
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()
# frame = img.copy()
# yuzler = yuz_cehresi.detectMultiScale(img, 1.1, 4)
# for (x, y, w, h) in yuzler:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
#     cv2.imshow("Yüz Algılama", frame)
#     if cv2.waitKey(1) == ord('q'):
#         break
# cv2.destroyAllWindows()
