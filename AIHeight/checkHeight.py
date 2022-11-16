import cv2

class height :
    def height(self, img):
        cascade_file = '../AIHeight/cascade/haarcascade_frontalface_alt.xml'
        cascade = cv2.CascadeClassifier(cascade_file)
        path = '../AIHeight/files'
        img_name = img
        full_path = path + '/' +img_name
        #검출하기
        imgOri = cv2.imread(full_path) 
        gray = cv2.cvtColor(imgOri, cv2.COLOR_BGR2GRAY) 
        face_list = cascade.detectMultiScale(gray, minSize = (50,50)) 
        yArr = []
        for (x, y, w, h) in face_list:
            color = (0, 0, 225) 
            pen_w = 2 
            cv2.rectangle(imgOri, (x, y), (x+w, y+h), color, thickness = pen_w)
            yArr.append(y)
        minY = 0
        maxY = 0
        for i in yArr:
            if i > maxY:
                minY = maxY
                maxY = i
            else:
                minY = i
        diffY = maxY - minY
        print("minY",minY,"maxY",maxY)
        print("diffY",diffY)
        result = "none"
        if diffY > 150:
            result = "family"
        print("result",result)
        return result
