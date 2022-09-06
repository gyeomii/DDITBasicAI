import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from keras import datasets, models, layers

labels = [
          "가",          
          "나",
          "다",
          "라",
          "마"
          ]

dirs = [
        "0",
        "1",
        "2",
        "3",
        "4",
      ]

train_images = np.load("train_image1.npy")
train_labels = np.load("train_label1.npy")
print("Train samples:", train_images.shape, train_labels.shape)

train_images = train_images/255.0

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(480, 640, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(5, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=15)
model.save("ganada.h5")

predictions = model.predict(train_images)

for i in range(450):
    print(i,np.argmax(predictions[i]))






