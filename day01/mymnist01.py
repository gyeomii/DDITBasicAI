
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical


(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print("train_images",train_images.shape)
print("train_labels",train_labels.shape)


print("test_images",test_images.shape)
print("test_labels",test_labels.shape)


print("train_labels[0]",test_labels[1])
for row in test_images[1]:
    for d in row:
        print(d,end="\t")
    print()

