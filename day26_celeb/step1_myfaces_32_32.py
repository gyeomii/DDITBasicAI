import os
import cv2
import random
import numpy as np

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

def originTo3232(from_file,to_file):
    img_array = np.fromfile(from_file, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    resize_img = cv2.resize(img, (32, 32))
    cv2.imwrite(to_file,resize_img)
    

for i in range(22):    
    files = os.listdir("train_origin/{}".format(labels[i]))
    for idx,f in enumerate(files):
        print("train_origin/{}/{}".format(labels[i],f),"train_image/{}/{}.png".format(100+i,idx))
        originTo3232("train_origin/{}/{}".format(labels[i],f),"train_image/{}/{}.png".format(100+i,idx))
    
    
    
# files = os.listdir("train_origin/{}".format(labels[0]))
# for idx,f in enumerate(files):
#     print("train_origin/{}/{}".format(labels[0],f),"train_image/{}/{}.png".format(100+0,idx))
#     originTo3232("train_origin/{}/{}".format(labels[0],f),"train_image/{}/{}.png".format(100+0,idx))
#
# files = os.listdir("train_origin/{}".format(labels[1]))
# for idx,f in enumerate(files):
#     print("train_origin/{}/{}".format(labels[1],f),"train_image/{}/{}.png".format(100+1,idx))
#     originTo3232("train_origin/{}/{}".format(labels[1],f),"train_image/{}/{}.png".format(100+1,idx))










