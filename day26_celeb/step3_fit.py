import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from keras import datasets, models, layers


labels = [
    "강동원",
    "공유",
    "권오중",
    "김종국",
    "리노",
    
    "마동석",
    "박명수",
    "박성웅",
    "박은빈",
    "수지",
    
    "아이유",
    "안유진",
    "예리",
    "오연서",
    "원빈",
    
    
    "장원영",
    "정소민",
    "조이",
    "채수빈",
    "천우희",
    
    "태연",
    "현빈"

  ]

train_images = np.load("train_image.npy")
train_labels = np.load("train_label.npy")


print("Train samples:", train_images.shape, train_labels.shape)


train_images = train_images/255.0

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(22, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=40)
model.save("celeb.h5")

test_loss, test_acc = model.evaluate(train_images, train_labels)

print('Test accuracy:', test_acc)

predictions = model.predict(train_images)

for i in range(218):
    print(i,np.argmax(predictions[i]))






