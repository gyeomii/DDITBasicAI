import cv2

img1 = cv2.imread('startup.png')
x = 330
y = 100
w = 500
h = 500
cropped = img1[y:y+h, x:x+w]
cv2.imshow('img1', cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()