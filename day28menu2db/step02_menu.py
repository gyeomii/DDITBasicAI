from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import tensorflow as tf
import numpy as np
from day28menu2db.menudao import MenuDao

dao = MenuDao()

labels = dao.getGroupMenu()

train_images_a = [
    [4, 9]
]

train_images_n = np.array(train_images_a)
train_images_n = train_images_n / (len(labels)-1) 
model =tf.keras.models.load_model("2.h5")

predictions = model.predict(train_images_n)

idx = np.argmax(predictions[0])

print(labels[idx])