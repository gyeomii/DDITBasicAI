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
        "0",
        "1",
        "2",
        "3",
        "4",
        "5"
      ]

train_label = []
train_image = np.empty((0, 0, 0),np.uint8)

cnt = 0

for i in range(6):
    files = os.listdir("train_eng/"+dirs[i])
    for f in files:
        train_image = np.append(train_image,cv2.imread('train_eng/'+dirs[i]+'/{}'.format(f)))
        train_label.append(i)
        cnt+=1
    
    


train_image = train_image.reshape((cnt,480,640,3))
train_label_n = np.array(train_label)

print(train_image.shape)
print(train_label_n)

np.save("train_image1",train_image)
np.save("train_label1",train_label_n)





