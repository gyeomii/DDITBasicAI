from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import numpy as np
from ai02.getBookNoAndKdcNo import getBookNo

dao = getBookNo()
row = dao.selectBookNoOfMember('aa')

print(row)




# userArr[int(inter1) + 6] = 1
# print(userArr)
userArr_n = np.array(row)
userArr_n =userArr_n.reshape((1, 10))
userArr_n = userArr_n.astype('float32') 
# print(userArr_n.shape)
print(userArr_n)
#
model = tf.keras.models.load_model('kdcBook.h5')
model.summary()
result = []
predict_result = model.predict(userArr_n)
print(predict_result)
for i in range(3):
    ai_answer = np.argmax(predict_result)
    print(ai_answer)
    result.append(ai_answer)
    predict_result[0][ai_answer] = -1
