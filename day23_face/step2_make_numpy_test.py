import numpy as np
import cv2
import random
from numpy import dtype
import os

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

test_label = []
test_image = np.empty((0, 0, 0),np.uint8)

cnt = 0

for i in range(23):
    files = os.listdir("test_image/"+dirs[i])
    for f in files:
        test_image = np.append(test_image,cv2.imread('test_image/'+dirs[i]+'/{}'.format(f)))
        test_label.append(i)
        cnt+=1
    
    


test_image = test_image.reshape((cnt,32,32,3))
test_label_n = np.array(test_label)

print(test_image.shape)
print(test_label_n)

np.save("test_image",test_image)
np.save("test_label",test_label_n)





