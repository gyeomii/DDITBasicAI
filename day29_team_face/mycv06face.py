import cv2

cascade_file = 'cascade/haarcascade_frontalface_alt.xml'
cascade = cv2.CascadeClassifier(cascade_file)

img = cv2.imread('1-2.jpg') 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
face_list = cascade.detectMultiScale(gray, minSize = (50,50)) 
count = 0
for (x, y, w, h) in face_list:
    color = (225, 0, 0) 
    pen_w = 3 
    face = img[y:y+h,x:x+h]

    path = "test_image"      
    resize_img = cv2.resize(face, (128, 128))
        
    cv2.imwrite("{}/{}-1.png".format(path,count), resize_img)   
    count += 1
    
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.imshow('img', img)
cv2.imwrite('temp.jpg', img) 
cv2.waitKey(0)
cv2.destroyAllWindows()
