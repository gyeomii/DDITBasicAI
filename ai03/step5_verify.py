from tensorboard.compat import tf
import numpy as np

labels = [
    "공유",
    "권오중",
    "김정화",
    "백승호",
    
    "손예진",
    "손흥민",
    "오바마",
    "오상욱",
    
    "오은영",
    "윤성빈",
    "이대은",
    "이효리",

    "정유미",
    "정은원",
    "제니",
    "한소희"
]

test_image_yous = np.load("test_imageGyeom.npy")
 
test_images = test_image_yous/255.0

model = tf.keras.models.load_model('celeb.h5')    #뇌 불러와서 predict 

predictions = model.predict(test_images)

idx_p = np.argmax(predictions)
print(labels[idx_p])
    
    
    
