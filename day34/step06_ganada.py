from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import cv2
import numpy as np

labels = [
          "기민혁",          
          "김성겸",
          "박수빈",
          "박지영",
          "윤재열",
          "채희진"
          ]

img1 = cv2.imread('train_eng/3/0.png')
print("img1",img1.shape)
train_images = img1.reshape((1,480,640,3))
train_images = train_images/255.0

model = tf.keras.models.load_model('teamVoice.h5')

predictions = model.predict(train_images)
l_idx = np.argmax(predictions[0])

print(l_idx,labels[l_idx])
    