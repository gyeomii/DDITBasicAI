from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import numpy as np
from ai06.memberMBTI import MBTI2

class AI_Module6:
    def recommandMBTIMovie(self,userArr,path):
        userArr_n = np.array(userArr)
        userArr_n =userArr_n.reshape((1, 8))
        userArr_n = userArr_n.astype('float32') 
        
        model = tf.keras.models.load_model(path)
    
        movie1 = 0
        movie2 = 0
        movie3 = 0
        result=[]
        predict_result = model.predict(userArr_n)
        # print(predict_result)
        for i in range(3):
            ai_answer = np.argmax(predict_result)
            result.append(ai_answer)
            predict_result[0][ai_answer] = -1
        # print(result)
        movie1= str(result[0])
        movie2= str(result[1])
        movie3= str(result[2])
        
        
        print(movie1,movie2,movie3)
        
        return movie1, movie2, movie3
    
    