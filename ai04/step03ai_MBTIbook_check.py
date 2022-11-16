from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import numpy as np
from ai04.mbti_book import MBTI

userArr = [0,0,0,0,0,0,0,0]
bookLabel = []
dao = MBTI()
row = dao.selectMBTI('jyp')
userArr = np.zeros(8)
bookLabel = []
print(row[2])
a=list(row[2])
print(a)

if a[0]=='I':
    userArr[0]=1
elif a[0]=='E':
    userArr[1]=1


if a[1]=='N':
    userArr[2]=1
elif a[1]=='S':
    userArr[3]=1


if a[2]=='F':
    userArr[4]=1
elif a[2]=='T':
    userArr[5]=1


if a[3]=='P':
    userArr[6]=1
elif a[3]=='J':
    userArr[7]=1

print(userArr)
