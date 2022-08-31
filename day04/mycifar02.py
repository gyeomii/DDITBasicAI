import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from keras import datasets, models, layers
import cv2

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']


(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
  
g_test_images = test_images 
print("Train samples:", train_images.shape, train_labels.shape)
print("Test samples:", test_images.shape, test_labels.shape)
 
train_images = train_images.reshape((50000, 32, 32, 3))
test_images = test_images.reshape((10000, 32, 32, 3))

 
 
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
model.add(layers.Dense(10, activation='softmax'))
 
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
 
model.fit(train_images, train_labels, epochs=5)
 
predictions = model.predict(test_images)




for idx, img in enumerate(g_test_images):
    go_label = test_labels[idx][0]
    ai_label = np.argmax(predictions[idx])
    print(go_label,ai_label)
    
    if go_label == ai_label:
        cv2.imwrite(f'test/o/{go_label}_{ai_label}_{idx}.jpg', img) 
    else:
        cv2.imwrite(f'test/x/{go_label}_{ai_label}_{idx}.jpg', img) 


