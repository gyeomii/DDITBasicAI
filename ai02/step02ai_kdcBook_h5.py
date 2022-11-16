from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import numpy as np

train_images = np.load("kdcBook_image.npy")
print(train_images.shape)
train_labels = np.load("kdcBook_label.npy")
print(train_labels.shape)

train_labels_c = to_categorical(train_labels, num_classes=2777)
print("train_labels_c",train_labels_c)
# print("len",train_labels_c[78])

model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(10,)))
# model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dense(2777, activation='softmax'))


model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])


model.fit(train_images, train_labels_c, epochs=100)

model.save("kdcBook.h5");

predict_result = model.predict(train_images)


print("predict_result",predict_result)
for r in predict_result:
    ai_answer = np.argmax(r)
    print(ai_answer)
