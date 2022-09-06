from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import cv2
import numpy as np

test_images = np.load("test_image1.npy")
test_labels = np.load("test_label1.npy")


test_images = test_images/255.0


print("Train samples:", test_images.shape, test_labels.shape)



model = tf.keras.models.load_model('ganada2.h5')


predictions = model.predict(test_images)

for i in range(5):
    print(np.argmax(predictions[i]))
    