import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from keras import datasets, models, layers


class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']


(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

np.save("train_images",train_images)
np.save("train_labels",train_labels)
np.save("test_images",test_images)
np.save("test_labels",test_labels)

