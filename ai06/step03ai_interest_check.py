from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import numpy as np
from ai06.memberMBTI import MBTI2

userArr = [0,0,0,0,0,0,0,0]
dao = MBTI2()
row = dao.selectMemberMBTI('cc')
mbti = row[0]
print(mbti)


if mbti[0] == 'E':
    userArr[0] = 1
if mbti[0] == 'I':
    userArr[1] = 1
if mbti[1] == 'N':
    userArr[2] = 1
if mbti[1] == 'S':
    userArr[3] = 1 
if mbti[2] == 'F':
    userArr[4] = 1
if mbti[2] == 'T':
    userArr[5] = 1             
if mbti[3] == 'P':
    userArr[6] = 1
if mbti[3] == 'J':
    userArr[7] = 1               

print(userArr)


