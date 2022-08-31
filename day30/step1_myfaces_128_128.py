
import cv2
import random

labels = ["곽금규",
          "곽동석",
          "기민혁",
          "김미정",
          "김민수",
          
          "김성겸",
          "김유미",
          "박건영",
          "박성우",
          "박수빈",
          
          "박수현",
          "박지영",
          "심재린",
          "양형주",
          "윤재열",
          
          "이상권",
          "이혜림",
          "장재훈",
          "조정현",
          "채희진",
          
          "최재혁",
          "한재웅",
          "한태훈"
          ]

dirs = [
        "00",
        "01",
        "02",
        "03",
        "04",
        
        "05",
        "06",
        "07",
        "08",
        "09",
        
        "10",
        "11",
        "12",
        "13",
        "14",
        
        "15",
        "16",
        "17",
        "18",
        "19",
        
        "20",
        "21",
        "22"
      ]

reverses = [
        True,
        True,
        True,
        False,
        True,
        
        True,
        False,
        True,
        False,
        True,
        
        True,
        False,
        True,
        True,
        True,
        
        True,
        True,
        True,
        True,
        False,
        
        True,
        True,
        True

      ]

def saveImage(label,dir,reverse):
    try:
        vidcap = cv2.VideoCapture('movie/{}.mp4'.format(label))
        
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
                
            path = "" 
            if random.random() > 0.16:
                path = "train_image"  
            else:
                path = "test_image"  
                
            resize_img = cv2.resize(img_save, (128, 128))    
                
            cv2.imwrite("{}/{}/{}.png".format(path,dir,count), resize_img)    
            
            count += 1
            # if count > 5:
            #     break
        
        vidcap.release()
        
    except:
        pass    

for i in range(23):
    saveImage(labels[i],dirs[i],reverses[i])




