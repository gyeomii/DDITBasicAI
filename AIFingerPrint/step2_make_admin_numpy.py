import os
import cv2
import numpy as np


labels = [
        "gyeom",
        "jiyoung",
        "jjae"
          ]



img = cv2.imread('./resizeImg/gyeom.png')


train_image = img.reshape((1,200*300*3))

np.save("gyeom",train_image)


print(train_image.shape)




