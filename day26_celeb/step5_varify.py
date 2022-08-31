
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import numpy as np

labels_yous = ["곽금규",
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

labels = [
    "강동원",
    "공유",
    "권오중",
    "김종국",
    "리노",
    
    "마동석",
    "박명수",
    "박성웅",
    "박은빈",
    "수지",
    
    "아이유",
    "안유진",
    "예리",
    "오연서",
    "원빈",
    
    
    "장원영",
    "정소민",
    "조이",
    "채수빈",
    "천우희",
    
    "태연",
    "현빈"

  ]

train_image_yous = np.load("train_image_yous.npy")
train_label_yous = np.load("train_label_yous.npy")

print("Train samples:", train_image_yous.shape, train_label_yous.shape)

train_image_yous = train_image_yous/255.0


model = tf.keras.models.load_model('celeb.h5')

predictions = model.predict(train_image_yous)

for i in range(5500):
    idx_l =  train_label_yous[i]
    idx_p = np.argmax(predictions[i])
    print(i, labels_yous[idx_l]   ,labels[idx_p])
    
