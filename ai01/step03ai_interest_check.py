from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import numpy as np
from ai01.ageGenderInterest import AGI

userArr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
bookLabel = []
dao = AGI()
row = dao.selectMemberAGI('jyp')
age = row[0]
gender = row[1]
inter1= row[2].split(',')[0]
print(age, gender, inter1)

if age <20:
    userArr[0] = 1
elif age >= 20 and age < 30:
    userArr[1] = 1
elif age >= 30 and age < 40:
    userArr[2] = 1
elif age >= 40 and age < 50:
    userArr[3] = 1
elif age >= 50:
    userArr[4] = 1

if gender == 'M':
    userArr[5] = 1
elif gender == 'F':
    userArr[6] = 1

userArr[int(inter1) + 6] = 1
print(userArr)
userArr_n = np.array(userArr)
userArr_n =userArr_n.reshape((1, 16))
userArr_n = userArr_n.astype('float32') 
print(userArr_n.shape)

model = tf.keras.models.load_model('interest.h5')
model.summary()
result = []
predict_result = model.predict(userArr_n)
print(predict_result)
for i in range(3):
    ai_answer = np.argmax(predict_result)
    print(ai_answer+1)
    result.append(ai_answer+1)
    predict_result[0][ai_answer] = -1
