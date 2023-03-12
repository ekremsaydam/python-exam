"""Haarcascade Example."""
import cv2 as cv
import imageio

# yüz cascade yüklemesi yüklemesi
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")


def detect(frame):
    # Gri renk şemasını görüntülemek
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # detectMultiScale() fonksiyonu ile daha nce yüklenen cascade filtresi uygulanır.
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    # 1.1 resmin ne kadar küçültüleceğinin oranıdır.
    # 5 değeri ise objenin minimum komşu sayısıdır.

    # Birden fazla tek frame içerisinde yüz olabilir.
    for x, y, w, h in faces:
        # Belirtilen yüzleri kırmızı diktörtgen içerisine almak.
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    return frame


# imageio ile video okunur.
reader = imageio.get_reader("video.mp4")
print(reader.get_meta_data())

# Videonun fps değeri okunur.
fps = reader.get_meta_data()["fps"]
print(fps, "fps")

# fps değeri ile okunan frameleri yazdırmak için nesne oluşturmak
writer = imageio.get_writer("output.mp4", fps=fps)

# Her bir frame için yüz tanımayı çalıştırmak.
for i, frame in enumerate(reader):
    frame = detect(frame)

    # Her bir frame output.mp4 dosyasına ekleniyor.
    writer.append_data(frame)
    cv.imshow("image", frame)
    if cv.waitKey(1) == ord("q"):
        break
    # Kaçıncı frame işleniyor
    print("frame number:", i)

# Dosya kapatılıyor.
writer.close()

cv.destroyAllWindows()
