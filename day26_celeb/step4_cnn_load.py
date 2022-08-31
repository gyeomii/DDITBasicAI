
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import numpy as np

train_images = np.load("train_image.npy")
train_labels = np.load("train_label.npy")

print("Train samples:", train_images.shape, train_labels.shape)

train_images = train_images/255.0


model = tf.keras.models.load_model('celeb.h5')

predictions = model.predict(train_images)

for i in range(210):
    print(i,np.argmax(predictions[i]))
    
