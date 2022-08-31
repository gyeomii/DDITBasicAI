import cv2

cascade_file = 'cascade/haarcascade_frontalface_alt.xml'
# cascade_file = 'cascade/haarcascade_frontalface_alt2.xml'
# cascade_file = 'cascade/haarcascade_frontalface_default.xml'
# cascade_file = 'cascade/haarcascade_frontalface_alt_tree.xml'
cascade = cv2.CascadeClassifier(cascade_file)

#검출하기
img = cv2.imread('1.png') 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
face_list = cascade.detectMultiScale(gray, minSize = (50,50)) 

for idx,(x, y, w, h) in enumerate(face_list):
    cropped = img[y:y+h, x:x+w]
    cv2.imshow('temp', cropped)
    cv2.imwrite(f'mem{idx}.jpg', cropped) 
    cv2.waitKey(0)
    
    print(x,y,w,h)
    color = (0, 0, 225) 
    pen_w = 3     
    cv2.rectangle(img, (x, y), (x+w, y+h), color, thickness = pen_w) 
    
    
    
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.imshow('img', img)
cv2.imwrite('temp.jpg', img) 
cv2.waitKey(0)
cv2.destroyAllWindows()
