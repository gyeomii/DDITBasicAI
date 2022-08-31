
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import numpy as np
import cv2

img1 = cv2.imread('0_0_1.jpg')
train_images = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
train_images = train_images.reshape((1,784))
print(train_images.shape)


model = tf.keras.models.load_model('mnist.h5')

predict_result = model.predict(train_images)


ai_answer = np.argmax(predict_result[0])
print("ai_answer",ai_answer)