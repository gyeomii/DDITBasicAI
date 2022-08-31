from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import tensorflow as tf
import numpy as np

labels = ["짜장면","짬뽕","순두부","돈까스","국밥"]

train_images_a = [
    [1,0,0,0,0,     0,1,0,0,0,      0,0,1,0,0]

]

train_images_n = np.array(train_images_a)
model =tf.keras.models.load_model("menu.h5")

predictions = model.predict(train_images_n)

idx = np.argmax(predictions[0])

print(labels[idx])