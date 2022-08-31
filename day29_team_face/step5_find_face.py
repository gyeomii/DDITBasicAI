
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from PIL import ImageFont, ImageDraw, Image
from tensorboard.compat import tf
import numpy as np
import cv2

labels = [
          "기민혁",          
          "김성겸",
          "박수빈",
          "박지영",
          "윤재열",
          "채희진"
          ]

dirs = [
        "00",
        "01",
        "02",
        "03",
        "14",
        "15"
      ]

cascade_file = 'cascade/haarcascade_frontalface_alt.xml'
cascade = cv2.CascadeClassifier(cascade_file)
model = tf.keras.models.load_model('face128_2.h5')

img = cv2.imread('1-3.jpg') 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
face_list = cascade.detectMultiScale(gray, minSize = (50,50)) 

for (x, y, w, h) in face_list:
    
    face = img[y:y+h,x:x+h]
    face_resize = cv2.resize(face,(128,128))
    face_resize = np.reshape(face_resize,(1,128,128,3))
    face_img = face_resize / 255.0
    
    predictions = model.predict(face_img)
    print(labels[np.argmax(predictions)])
    
    color = (225, 0, 0) 
    pen_w = 3 
    cv2.rectangle(img, (x, y), (x+w, y+h), color, thickness = pen_w) 
    
    font = ImageFont.truetype("HMFMPYUN.TTF", 30)
    img_pil = Image.fromarray(img)
    idraw = ImageDraw.Draw(img_pil)
    idraw.text((x, y), labels[np.argmax(predictions)], font=font)
    img = np.array(img_pil)

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
