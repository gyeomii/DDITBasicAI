import numpy as np
import cv2
import random
from numpy import dtype
import os

labels = [
    "강동원",
    "공유",
    "권오중",
    "김종국",
    "리노",
    
    "마동석",
    "박명수",
    "박성웅",
    "박은빈",
    "수지",
    
    "아이유",
    "안유진",
    "예리",
    "오연서",
    "원빈",
    
    
    "장원영",
    "정소민",
    "조이",
    "채수빈",
    "천우희",
    
    "태연",
    "현빈"

  ]




train_label = []
train_image = np.empty((0, 0, 0),np.uint8)

cnt = 0

for i in range(22):
    files = os.listdir("train_image/"+str(100+i))
    for f in files:
        train_image = np.append(train_image,cv2.imread('train_image/'+str(100+i)+'/{}'.format(f)))
        train_label.append(i)
        cnt+=1
    
train_image = train_image.reshape((cnt,32,32,3))
train_label_n = np.array(train_label)

np.save("train_image",train_image)
np.save("train_label",train_label_n)




print(train_image.shape)
print(train_label_n)



