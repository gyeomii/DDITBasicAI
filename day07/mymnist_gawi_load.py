
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import numpy as np

train_images_a = [[1]]
train_images = np.array(train_images_a)
model = tf.keras.models.load_model('mnist_gawi.h5')
predict_result = model.predict(train_images)
ai_answer = np.argmax(predict_result[0])

print("ai_answer",ai_answer)