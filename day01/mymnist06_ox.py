import numpy as np
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical


(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

g_train_labels = train_labels


train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255


train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)


model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(layers.Dense(10, activation='softmax'))


model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5, batch_size=128)
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('test_acc: ', test_acc)

predict_result = model.predict(train_images)


cnt_o = 0
cnt_x = 0
for i in range(60000):
    go_label = g_train_labels[i]
    ai_label = np.argmax(predict_result[i])
    if go_label == ai_label :
        cnt_o += 1
    else:
        cnt_x += 1
        
        

print("cnt_o",cnt_o/60000)
print("cnt_x",cnt_x/60000)


