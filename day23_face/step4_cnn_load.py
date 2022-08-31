
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import numpy as np

train_images = np.load("train_image.npy")
train_labels = np.load("train_label.npy")
test_images = np.load("test_image.npy")
test_labels = np.load("test_label.npy")

train_images = train_images/255.0
test_images = test_images/255.0

print("Train samples:", train_images.shape, train_labels.shape)
print("Test samples:", test_images.shape, test_labels.shape)


model = tf.keras.models.load_model('face.h5')

predictions = model.predict(test_images)

for i in range(1022):
    print(i,np.argmax(predictions[i]))
    
