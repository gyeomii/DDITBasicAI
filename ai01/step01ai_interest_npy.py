from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import numpy as np
from ai01.makeTrainSet import DS
# DB에서 데이터 가져오기
dao = DS()
imageRows = dao.selectTrainImage()
labelRows = dao.selectTrainLabel()

# 배열 생성
trainImage_a = []
trainLabel_a = []

# trainImage 배열담기
for row in imageRows:
    trainImage_a.append(list(row))
trainImage = np.array(trainImage_a)
print(trainImage.shape)
print(trainImage)

# trainLabel 배열담기
for label in labelRows:
    trainLabel_a.append(label[0]-1)
trainLabel = np.array(trainLabel_a)
print(trainLabel.shape)
print(trainLabel)

np.save("interest_image",trainImage)
np.save("interest_label",trainLabel)