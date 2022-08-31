import cv2

img1 = cv2.imread('startup.png')

cv2.putText(img1,"SUJI",(470,200),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

cv2.imshow('img1', img1)


cv2.waitKey(0)
cv2.destroyAllWindows()