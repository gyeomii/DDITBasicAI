from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import numpy as np
from ai05.movieLinkRating import MOR


dao = MOR()
row = dao.selectMovieHistory('cc')
genre0 = 0
genre1 = 0
genre2 = 0
genre3 = 0
genre4 = 0
genre5 = 0

for r in row:
    genre = dao.selectMovieGenre(r[0])[0]
    print(genre)
    if genre == 0:
        genre0 += 1
    elif genre == 1:
        genre1 += 1
    elif genre == 2:
        genre2 += 1
    elif genre == 3:
        genre3 += 1
    elif genre == 4:
        genre4 += 1
    elif genre == 5:
        genre5 += 1

print(genre0, genre1,genre2,genre3, genre4,genre5)
max = 0
maxVal = 0
if genre0 > max:
    max = genre0
    maxVal = 0
elif genre1 > max:
    max = genre0
    maxVal = 1
elif genre2 > max:
    max = genre1
    maxVal = 2
elif genre3 > max:
    max = genre2
    maxVal = 3
elif genre4 > max:
    max = genre3
    maxVal = 4
elif genre5 > max:
    max = genre4
    maxVal = 5
    
if max<2 :
    max = 0
elif max>=2 and max <5 :
    max = 1
elif max>=5 :
    max = 2
    
userArr =[maxVal,max]
print(userArr)

userArr_n = np.array(userArr)
userArr_n =userArr_n.reshape((1, 2))
userArr_n = userArr_n.astype('float32') 
print(userArr_n.shape)

model = tf.keras.models.load_model('movieAI.h5')
model.summary()
result = []
predict_result = model.predict(userArr_n)
print(predict_result)
for i in range(3):
    ai_answer = np.argmax(predict_result)
    print(ai_answer)
    result.append(ai_answer)
    predict_result[0][ai_answer] = -1
