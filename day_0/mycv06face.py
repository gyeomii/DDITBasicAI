import cv2

cascade_file = 'cascade/haarcascade_smile.xml'
cascade = cv2.CascadeClassifier(cascade_file)

#검출하기
img = cv2.imread('startup.png') 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
face_list = cascade.detectMultiScale(gray, minSize = (50,50)) 

for (x, y, w, h) in face_list:
    color = (0, 0, 225) 
    pen_w = 3 
    cv2.rectangle(img, (x, y), (x+w, y+h), color, thickness = pen_w) 
    
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.imshow('img', img)
cv2.imwrite('temp.jpg', img) 
cv2.waitKey(0)
cv2.destroyAllWindows()
