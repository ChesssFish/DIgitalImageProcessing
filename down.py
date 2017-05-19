import cv2
import sys
img = cv2.imread("kkk.jpg")

x = 1
while x <= 128:
  for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
      img[i][j] /= x
      img[i][j] *= x
      img[i][j] += x/2

  cv2.imshow("Level = "+str(256 / x), img)
  cv2.moveWindow("Level = "+str(256 / x), 0, 0)
  cv2.waitKey(0)
  x *= 2
cv2.destroyAllWindows()