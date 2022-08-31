from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import numpy as np
from keras.integration_test.preprocessing_test_utils import BATCH_SIZE

ti1 = np.load("omok_train6.npy")


tl1 = np.load("omok_answer6.npy")




train_images = ti1
train_labels = tl1

np.save("train_images",train_images)

print(train_images.shape)
print(train_labels.shape)

train_labels_c = to_categorical(train_labels,num_classes=400)
print("train_labels_c",train_labels_c)

model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(400,)))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(1024, activation='relu'))
model.add(layers.Dense(1024, activation='relu'))
model.add(layers.Dense(400, activation='softmax'))


model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])


model.fit(train_images, train_labels_c, epochs=100, batch_size=4096)
model.save('alphao6.h5')

predict_result = model.predict(train_images)
print("predict_result",predict_result)
for r in predict_result:
    ai_answer = np.argmax(r)
    ii = int(ai_answer / 20)
    jj = ai_answer % 20
    print(ai_answer,ii,jj,end=",")
    print()




