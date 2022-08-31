import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from keras import datasets, models, layers
import cv2


class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']


(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

print(train_images.shape)
print(train_images[0])

  
for idx,img in enumerate(train_images):
    cv2.imwrite('train_image/'+str(idx)+'.png', train_images[idx]) 
    if idx > 100:
        break
    



