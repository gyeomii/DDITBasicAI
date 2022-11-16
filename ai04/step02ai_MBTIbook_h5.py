from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import numpy as np

train_images = np.load("MBTIbook_image.npy")
print(train_images.shape)
train_labels = np.load("MBTIbook_label.npy")
print(train_labels.shape)

train_labels_c = to_categorical(train_labels, num_classes=48)
print("train_labels_c",train_labels_c)
print("len",len(train_labels_c))

model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(8,)))
model.add(layers.Dense(1024, activation='relu'))
model.add(layers.Dense(48, activation='softmax'))


model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])


model.fit(train_images, train_labels_c, epochs=40, batch_size=50)

model.save("mbti_book.h5");

predict_result = model.predict(train_images)


print("predict_result",predict_result)
for r in predict_result:
    ai_answer = np.argmax(r)
    print(ai_answer)
