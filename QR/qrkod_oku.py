import cv2
from pyzbar import pyzbar  # pip install pyzbar


def barkod_oku(frame):
    barcodes = pyzbar.decode(frame)
    # print(barcodes)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        barcode_info = barcode.data.decode('utf-8')
        #color = BGR
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # font = cv2.FONT_HERSHEY_DUPLEX
        # font = cv2.FONT_HERSHEY_SIMPLEX
        font = cv2.FONT_HERSHEY_PLAIN
        textsize = cv2.putText(frame, barcode_info, (x, y+h+20),
                               font, 1.0, (255, 255, 255), 1)
        print(textsize)
        with open('okunan_barkod.txt', mode='w', encoding='utf-8') as file:
            file.write('Okunan Barkod:'+barcode_info)

    return frame


def main():
    kamera = cv2.VideoCapture(0)
    while True:
        ret, frame = kamera.read()
        frame = barkod_oku(frame=frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    kamera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
