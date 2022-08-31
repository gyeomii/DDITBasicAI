
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import numpy as np
import cv2



labels = ["곽금규",
          "곽동석",
          "기민혁",
          "김미정",
          "김민수",
          
          "김성겸",
          "김유미",
          "박건영",
          "박성우",
          "박수빈",
          
          "박수현",
          "박지영",
          "심재린",
          "양형주",
          "윤재열",
          
          "이상권",
          "이혜림",
          "장재훈",
          "조정현",
          "채희진",
          
          "최재혁",
          "한재웅",
          "한태훈"
          ]

labels_team = [
    "박수빈",
    "기민혁",
    "박지영",
    "채희진",
    "윤재열",
    "김성겸"
    ]


img1 = cv2.imread('1-2.jpg')
resize_img = cv2.resize(img1, (128, 128))
print(resize_img.shape)
resize_img = np.reshape(resize_img,(1,128,128,3))
test_images = resize_img/255.0



model = tf.keras.models.load_model('face128_2.h5')
predictions = model.predict(test_images)

for i in range(6):
    idx_label= np.argmax(predictions[i])
    print(i,labels[idx_label])
#

