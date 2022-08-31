import cv2

img1 = cv2.imread('startup.png')
resize_img = cv2.resize(img1, (500, 300))
cv2.imshow('resize_img', resize_img)


cv2.waitKey(0)
cv2.destroyAllWindows()