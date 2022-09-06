from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import matplotlib.pyplot as plt

import cv2 as cv
import numpy as np

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()





train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255


train_labels = to_categorical(train_labels)
test_labels_shape = to_categorical(test_labels)

model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(layers.Dense(10, activation='softmax'))

# 모델 컴파일 하기
model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])


history = model.fit(train_images, train_labels, epochs=5, batch_size=128)

print(history)

plt.plot(history.history['accuracy'])
plt.plot(history.history['loss'])
plt.legend(['training', 'validation'], loc = 'upper left')
plt.show()