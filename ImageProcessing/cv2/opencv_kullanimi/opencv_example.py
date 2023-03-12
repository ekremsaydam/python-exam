"""OpenCV ile calismak."""
import cv2

img = cv2.imread("logo2.png", cv2.IMREAD_GRAYSCALE)
# img = cv2.imread("logo2.png", cv2.IMREAD_COLOR)
cv2.imwrite("logo2_gray.png", img)
cv2.imshow(winname="image", mat=img)
cv2.waitKey(0)
cv2.destroyAllWindows()
