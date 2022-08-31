
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import numpy as np
import cv2

img1 = cv2.imread('9.jpg')
resize_img = cv2.resize(img1, (28, 28))
train_images = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)
cv2.imshow('dst1', train_images)
train_images = 255 - train_images
cv2.imshow('dst2', train_images)

train_images = train_images.reshape((1,784))
train_images = train_images.astype('float32') / 255



print(train_images.shape)


model = tf.keras.models.load_model('mnist.h5')

predict_result = model.predict(train_images)


ai_answer = np.argmax(predict_result[0])
print("ai_answer",ai_answer)


cv2.waitKey(0)
cv2.destroyAllWindows()