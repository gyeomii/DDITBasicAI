import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from keras.utils import to_categorical
from keras import datasets, layers, models


labels = [
        "gyeom",
        "jiyoung",
        "jjae"
          ]


train_images = np.load("train_image.npy")
train_labels = np.load("train_label.npy")
train_labels_c = to_categorical(train_labels)
print("train_labels_c",train_labels_c)
print("Train samples:", train_images.shape, train_labels.shape)
 


train_images = train_images / 255.0

model = models.Sequential()
model.add(layers.Dense(12, activation='relu', input_shape=(200*300*3,)))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(3, activation='softmax'))

# model.add(layers.Dense(22, activation='softmax'))

model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

model.summary()
model.fit(train_images, train_labels_c, epochs=100)
#model.save("finger.h5")

predictions = model.predict(train_images)

for i in range(12):
    print(i,np.argmax(predictions[i]))
 
