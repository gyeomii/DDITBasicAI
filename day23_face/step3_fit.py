import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from keras import datasets, models, layers


labels = ["곽금규",
          "곽동석",
          "기민혁",
          "김미정",
          "김민수",
          
          "김성겸",
          "김유미",
          "박건영",
          "박성우",
          "박수빈",
          
          "박수현",
          "박지영",
          "심재린",
          "양형주",
          "윤재열",
          
          "이상권",
          "이혜림",
          "장재훈",
          "조정현",
          "채희진",
          
          "최재혁",
          "한재웅",
          "한태훈"
          ]

train_images = np.load("train_image.npy")
train_labels = np.load("train_label.npy")
test_images = np.load("test_image.npy")
test_labels = np.load("test_label.npy")

print("Train samples:", train_images.shape, train_labels.shape)
print("Test samples:", test_images.shape, test_labels.shape)
 

train_images = train_images/255.0
test_images = test_images/255.0

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(23, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10)
model.save("face.h5")

test_loss, test_acc = model.evaluate(test_images, test_labels)

print('Test accuracy:', test_acc)

predictions = model.predict(test_images)

for i in range(1022):
    print(i,np.argmax(predictions[i]))






