from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import tensorflow as tf
import numpy as np
import cv2
class FingerPrint:
    def varify(self, imgName):
        labels = [
                "gyeom",
                "jiyoung",
                "jjae"
                  ]
        
        
        path = 'D:/workspace_python/AI_Recommand/AIFingerPrint/files'
        img_name = imgName
        full_path = path + '/' +img_name
        print(full_path)
        
        img = cv2.imread(full_path)
        train_image = img.reshape((1,200*300*3))
        
        
        # train_image_yous = np.load("gyeom.npy")
        #
        # print("Train samples:", train_image_yous.shape)
        
        train_image_yous = train_image / 255.0
        
        model = tf.keras.models.load_model('finger.h5')
        
        predictions = model.predict(train_image_yous)
        idx = np.argmax(predictions)
        print(labels[idx])
        name = img_name.split('.')[0]
        print(name)
        isCorrect = ''
        if name == labels[idx]:
            isCorrect =  'True'
        else:
            isCorrect =  'False'
        print(isCorrect)
        return isCorrect
