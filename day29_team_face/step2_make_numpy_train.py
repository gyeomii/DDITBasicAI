import numpy as np
import cv2
import random
from numpy import dtype
import os

labels = [
          "기민혁",          
          "김성겸",
          "박수빈",
          "박지영",
          "윤재열",
          "채희진"
          ]

dirs = [

        "00",
        "01",
        "02",
        "03",
        "04",
        "05"
      ]


train_label = []
train_image = np.empty((0, 0, 0),np.uint8)

cnt = 0

for i in range(6):
    files = os.listdir("train_image3/"+dirs[i])
    for f in files:
        train_image = np.append(train_image,cv2.imread('train_image3/'+dirs[i]+'/{}'.format(f)))
        train_label.append(i)
        print(cnt)
        cnt+=1
    
    
# files = os.listdir("train_image/"+dirs[1])
# for f in files:
#     train_image = np.append(train_image,cv2.imread('train_image/'+dirs[1]+'/{}'.format(f)))
#     train_label.append(1)  
#     cnt+=1  
#
# files = os.listdir("train_image/02")
# for f in files:
#     train_image = np.append(train_image,cv2.imread('train_image/02/{}'.format(f)))
#     train_label.append(2)  
#     cnt+=1      

train_image = train_image.reshape((cnt,128,128,3))
train_label_n = np.array(train_label)

np.save("train_image3",train_image)
np.save("train_label3",train_label_n)





