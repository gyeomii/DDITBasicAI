import numpy as np
import cv2
import random

labels = [
        "기민혁",          
        "김성겸",
        "박수빈",
        "박지영",
        "윤재열",
        "채희진"
          ]

dirs = [
        "02",
        "05",
        "09",
        "11",
        "14",
        "19"
      ]

reverses = [
        False,
        False,
        True,
        True,
        True,
        True
      ]

def saveImage(label,dir,reverse):
    try:
        vidcap = cv2.VideoCapture(f'movie/{label}.mp4')
        
        count = 0
        while(vidcap.isOpened()):
            ret, src = vidcap.read()
        
            height, width, channel = src.shape
            matrix = cv2.getRotationMatrix2D((width/2, height/2), 180, 1)
            dst = cv2.warpAffine(src, matrix, (width, height))
        
            print(dst.shape)
            img_save = None
            if reverse:
                img_save = dst
            else:
                img_save = src
            
            cascade_file = 'cascade/haarcascade_frontalface_alt.xml'
            cascade = cv2.CascadeClassifier(cascade_file)
            
            img = img_save
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
            face_list = cascade.detectMultiScale(gray, minSize = (50,50)) 
            
            for (x, y, w, h) in face_list:
                color = (225, 0, 0) 
                pen_w = 3 
                
                face = img[y:y+h,x:x+h]
                # face_n = np.array(face)
                # print(face.shape)
                # face_n.resize(1,64,64,3)
                # print(face_n.shape)
            
                path = "train_image3"      
                resize_img = cv2.resize(face, (128, 128))
                    
                cv2.imwrite("{}/{}/{}.png".format(path,dir,count), resize_img)    
                
                count += 1
                # if count > 5:
                #     break
        
        vidcap.release()
        
    except:
        pass    

for i in range(6):
    saveImage(labels[i],dirs[i],reverses[i])




