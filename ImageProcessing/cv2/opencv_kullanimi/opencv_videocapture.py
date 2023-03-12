"""OpenCV VideoCapture."""
import cv2

# 0 index de bulunan kameranın video kaydını başlatır.
cap = cv2.VideoCapture(0)

# Video kaydının başlayıp başlamadığının kontrolü
if not cap.isOpened():
    print("Video capture acilamiyor.")
    exit()

while True:
    ret, frame = cap.read()  # video karelerinin (frame) okuma
    if not ret:
        print("Karaler yakalanamıyor.")
        break

    src = cv2.cvtColor(frame, cv2.IMREAD_COLOR)

    # istenilen renk şemasına çevirme
    srcgray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    height, width = srcgray.shape
    srcgray_dimension = (int(width * 1.5), int(height * 1.5))
    src_resize = cv2.resize(srcgray, srcgray_dimension)

    src_resize_height, src_resize_width = src_resize.shape
    src_resize_center = (src_resize_width // 2, src_resize_height // 2)

    # istendik kadar döndürmek veya zoom yapmak.
    M = cv2.getRotationMatrix2D(src_resize_center, -45, 1.0)
    src_resize_rotate = cv2.warpAffine(
        src_resize, M, (src_resize_width, src_resize_height)
    )

    ksize = (15, 15)
    sigmaX = 2
    src_resize_rotate_blured = cv2.GaussianBlur(src_resize_rotate, ksize, sigmaX)
    # cv2.imshow -> Görüntünün işlendikten sonra görüntülenmesini sağlar.
    cv2.imshow("source", src)  # src kaydını gösterme
    cv2.imshow("resize", src_resize)  # src_resize kaydını gösterme
    cv2.imshow("Rotate", src_resize_rotate)  # src_resize_rotate kaydını gösterme
    cv2.imshow("Blured", src_resize_rotate_blured)  # src_resize_rotate kaydını gösterme

    # pt1 -> Başlangıç noktası
    # pt2 -> Bitiş noktası
    # color -> (Blue,Green,Red)
    src_rectangle = cv2.rectangle(
        img=src, pt1=(15, 15), pt2=(350, 250), color=(0, 0, 255), thickness=1
    )

    src_circle = cv2.circle(
        img=src, center=(150, 150), radius=50, color=(0, 255, 0), thickness=2
    )
    src_line = cv2.line(
        img=src, pt1=(20, 20), pt2=(50, 50), color=(255, 0, 0), thickness=3
    )

    src_put_text = cv2.putText(
        img=src,
        text="Merhaba",
        org=(src.shape[1] - 150, src.shape[0] - 150),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=1,
        color=(200, 100, 50),
        thickness=5,
    )

    cv2.imshow("Rectangle", src_put_text)
    # cv2.waitkey -> pencere gösteriminden sonra bir tuşa basılmasını bekler.
    if cv2.waitKey(1) == ord("q"):
        break

# Kamera objelerini RAM üzerinden temizlemek için release ve destroyAllWindows komutları uygulanır.
cap.release()
cv2.destroyAllWindows()
