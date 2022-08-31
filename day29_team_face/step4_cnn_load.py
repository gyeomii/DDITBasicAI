
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import numpy as np

test_images = np.load("test_image3.npy")
test_labels = np.load("test_label3.npy")


test_images = test_images/255.0


print("Train samples:", test_images.shape, test_labels.shape)



model = tf.keras.models.load_model('face128_2.h5')

test_loss, test_acc = model.evaluate(test_images, test_labels)

predictions = model.predict(test_images)

for i in range(18):
    print(i,np.argmax(predictions[i]))
    
