"""Yüz, yaş ve cinsiyet tanıma."""
# Import Libraries
import cv2  # pip install opencv-python
import numpy as np

# Cinsiyet model mimarisi
# https://talhassner.github.io/home/publication/2015_CVPR
GENDER_MODEL = 'model/gender_deploy.prototxt'
# Cinsiyet modeli önceden eğitilmiş öngörü
GENDER_PROTO = 'model/gender_net.caffemodel'
# Ortalama
MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
# Cisniyet Bilgisi
GENDER_LIST = ['Erkek', 'Kadın']
# https://raw.githubusercontent.com/opencv/opencv/master/samples/dnn/face_detector/deploy.prototxt
FACE_PROTO = "model/face_deploy.prototxt"
# https://raw.githubusercontent.com/opencv/opencv_3rdparty/dnn_samples_face_detector_20180205_fp16/res10_300x300_ssd_iter_140000_fp16.caffemodel
FACE_MODEL = "model/res10_300x300_ssd_iter_140000_fp16.caffemodel"
# Yaş için model mimarisi
AGE_MODEL = 'model/gender_deploy.prototxt'
# Önceden eğitilmiş bilgisayar görüsü.
AGE_PROTO = 'model/gender_net.caffemodel'
# 8 tane CNN olasılık katmanı
AGE_INTERVALS = ['(0, 2)', '(4, 6)', '(8, 12)', '(15, 20)',
                 '(25, 32)', '(38, 43)', '(48, 53)', '(60, 100)']
# Çerçeve boyutunu
frame_width = 1280
frame_height = 720
# Yüz tanıma Caffe modelini yüklemek
face_net = cv2.dnn.readNetFromCaffe(FACE_PROTO, FACE_MODEL)
# Yaş tahmin modelini yüklemek
age_net = cv2.dnn.readNetFromCaffe(AGE_MODEL, AGE_PROTO)
# Cinsiyet tahmin modelini yüklemek
gender_net = cv2.dnn.readNetFromCaffe(GENDER_MODEL, GENDER_PROTO)


def get_faces(frame, confidence_threshold=0.5):
    # frame i blob verisine dönüştürmek.
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104, 177.0, 123.0))
    # yük tanıma verisi olarak blob veriyi almak.
    face_net.setInput(blob)
    # tahminleri almak.
    output = np.squeeze(face_net.forward())
    # sonuç listesi içeriği oluşturmak
    faces = []
    # Algılanan yüzler üzerinde döngü
    for i in range(output.shape[0]):
        confidence = output[i, 2]
        if confidence > confidence_threshold:
            box = output[i, 3:7] * \
                np.array([frame.shape[1], frame.shape[0],
                         frame.shape[1], frame.shape[0]])
            # tam sayıya dönültürme
            start_x, start_y, end_x, end_y = box.astype(np.int)
            # çerçeveyi genişlet.
            start_x, start_y, end_x, end_y = start_x - \
                10, start_y - 10, end_x + 10, end_y + 10
            start_x = 0 if start_x < 0 else start_x
            start_y = 0 if start_y < 0 else start_y
            end_x = 0 if end_x < 0 else end_x
            end_y = 0 if end_y < 0 else end_y
            # append to our list
            faces.append((start_x, start_y, end_x, end_y))
    return faces


# from: https://stackoverflow.com/questions/44650888/resize-an-image-without-distortion-opencv
def image_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    # görüntü boyutunu değiştirme
    dim = None
    (h, w) = image.shape[:2]
    # genişlik ve yükseklik yok ise resim boyutunu al.
    if width is None and height is None:
        return image
    # genişliğin olup olmadığını kontrol et.
    if width is None:
        # yükseklik oranını hesaplayın.
        r = height / float(h)
        dim = (int(w * r), height)
    # Yükseklik yok ise
    else:
        # Genişlik oranını hesaplayın.
        r = width / float(w)
        dim = (width, int(h * r))
    # resmi yeniden boyutlandırma.
    return cv2.resize(image, dim, interpolation=inter)


def get_gender_predictions(face_img):
    blob = cv2.dnn.blobFromImage(
        image=face_img, scalefactor=1.0, size=(227, 227),
        mean=MODEL_MEAN_VALUES, swapRB=False, crop=False
    )
    gender_net.setInput(blob)
    return gender_net.forward()


def get_age_predictions(face_img):
    blob = cv2.dnn.blobFromImage(
        image=face_img, scalefactor=1.0, size=(227, 227),
        mean=MODEL_MEAN_VALUES, swapRB=False
    )
    age_net.setInput(blob)
    return age_net.forward()


def predict_age_and_gender():
    """Resimde gösterilen yüzlerin cinsiyetini tahmin edin"""
    # yeni bir kamera nesnesi oluştur
    cap = cv2.VideoCapture(0)

    while True:
        _, img = cap.read()
        # Görüntünün bir kopyasını alın
        frame = img.copy()
        # ve yeniden boyutlandırın
        if frame.shape[1] > frame_width:
            frame = image_resize(frame, width=frame_width)
        # yüzleri tahmin et
        faces = get_faces(frame)
        # Algılanan yüzler üzerinde döngü
        # Algılanan yüzlerin koordinat bilgileri üzerinde döngü
        for i, (start_x, start_y, end_x, end_y) in enumerate(faces):
            face_img = frame[start_y: end_y, start_x: end_x]
            # yaşı tahmin et
            age_preds = get_age_predictions(face_img)
            # cinsiyeti tahmin et
            gender_preds = get_gender_predictions(face_img)
            i = gender_preds[0].argmax()
            gender = GENDER_LIST[i]
            gender_confidence_score = gender_preds[0][i]
            i = age_preds[0].argmax()
            age = AGE_INTERVALS[i]
            age_confidence_score = age_preds[0][i]
            # kutuyu çiz
            label = f"{gender}-{gender_confidence_score*100:.1f}%, {age}-{age_confidence_score*100:.1f}%"
            # label = "{}-{:.2f}%".format(gender, gender_confidence_score*100)
            print(label)
            yPos = start_y - 15
            while yPos < 15:
                yPos += 15
            box_color = (255, 0, 0) if gender == "Erkek" else (147, 20, 255)
            cv2.rectangle(frame, (start_x, start_y),
                          (end_x, end_y), box_color, 2)
            # Etiket işlenmiş görüntü
            cv2.putText(frame, label, (start_x, yPos),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.54, box_color, 2)

            # İşlenmiş görüntüyü göster
        cv2.imshow("Gender Estimator", frame)
        if cv2.waitKey(1) == ord("q"):
            break
        # resmi kaydetmek istiyorsanız
        # cv2.imwrite("output.jpg", frame)
    # Temizlemek
    cv2.destroyAllWindows()


if __name__ == "__main__":
    predict_age_and_gender()
