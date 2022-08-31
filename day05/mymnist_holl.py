from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import numpy as np

train_images_a = [
    [0,0],
    [0,1],
    [1,0],
    [1,1]
]
train_labels_a = [
    0,1,1,0
]

train_images = np.array(train_images_a)
train_labels = np.array(train_labels_a)

train_labels_c = to_categorical(train_labels)
print("train_labels_c",train_labels_c)

model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(2,)))
model.add(layers.Dense(2, activation='softmax'))


model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

model.fit(train_images, train_labels_c, epochs=5)
test_loss, test_acc = model.evaluate(train_images, train_labels_c)
print('test_acc: ', test_acc)


predict_result = model.predict(train_images)
print("predict_result",predict_result)



