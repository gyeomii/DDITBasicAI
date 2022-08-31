from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import numpy as np

train_images_a = [
    [1,0,0,0,0,     0,1,0,0,0,      0,0,1,0,0],
    [0,1,0,0,0,     0,0,1,0,0,      0,0,0,1,0],
    [0,0,1,0,0,     0,0,0,1,0,      0,0,0,0,1],
    [0,0,0,1,0,     0,0,0,0,1,      1,0,0,0,0],
    [0,0,0,0,1,     1,0,0,0,0,      0,1,0,0,0]
]

train_labels_a = [
    3,4,0,1,2
]

train_images = np.array(train_images_a)
train_labels = np.array(train_labels_a)

train_labels_c = to_categorical(train_labels)
print("train_labels_c",train_labels_c)

model = models.Sequential()
model.add(layers.Dense(1024, activation='relu', input_shape=(15,)))
model.add(layers.Dense(1024, activation='relu'))
model.add(layers.Dense(5, activation='softmax'))


model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])


model.fit(train_images, train_labels_c, epochs=20)


model.save("menu.h5");

predict_result = model.predict(train_images)
print("predict_result",predict_result)
for r in predict_result:
    ai_answer = np.argmax(r)
    print(ai_answer,end=",")



