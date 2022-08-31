import cv2

img1 = cv2.imread('Lenna.png')
dst = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

cv2.imshow('img1', dst)
cv2.imwrite('Lenna.jpg', dst) 

cv2.waitKey(0)
cv2.destroyAllWindows()