from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import numpy as np

train_images_a = [
    [0,0,0,0],
    [-1,0,0,0],
    [1,-1,0,0],
    [-1,-1,-1,-1]
    
]
train_labels_a = [
    0,1,3,3
]

train_images = np.array(train_images_a)
train_labels = np.array(train_labels_a)

train_labels_c = to_categorical(train_labels)
print("train_labels_c",train_labels_c)

model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(4,)))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(4, activation='softmax'))


model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])


model.fit(train_images[0:3], train_labels_c[0:3], epochs=10)

predict_result = model.predict(train_images[0:3])
print("predict_result",predict_result)
for r in predict_result:
    ai_answer = np.argmax(r)
    ii = int(ai_answer / 2)
    jj = ai_answer % 2
    print(ai_answer,ii,jj,end=",")
    print()




