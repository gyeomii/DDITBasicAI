import os
import cv2
import numpy as np


labels = [
        "gyeom",
        "jiyoung",
        "jjae"
          ]


train_lable = []
train_image = np.empty((0, 0, 0),np.uint8)

cnt=0

for i in range(4):
    j = 0
    files = os.listdir("resizeImg/")
    # print(files)
    for f in files:
        print(f)
        img = cv2.imread('resizeImg/{}'.format(f))
        rotate = img
        if i == 1:
            rotate = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        elif i == 2:
            rotate = cv2.rotate(img, cv2.ROTATE_180)
        elif i == 3 :
            rotate = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
            
        train_image = np.append(train_image,rotate)
        print(train_image.shape)
        train_lable.append(j)
        j+=1
        cnt+=1
    


train_image = train_image.reshape((cnt,200*300*3))
train_lable_n = np.array(train_lable)

np.save("train_image",train_image)
np.save("train_label",train_lable_n)

# cv2.imshow("강동원",train_image[0])

print(train_image.shape)
print(train_lable_n)

# cv2.waitKey(0)
# cv2.destroyAllWindows()




