from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import numpy as np

class AI_Module2:
    def recommandBook(self,userArr,path):
        userArr_n = np.array(userArr)
        userArr_n = userArr_n.reshape((1, 10))
        userArr_n = userArr_n.astype('float32') 
        
        model = tf.keras.models.load_model(path)
    
        book1 = 0
        book2 = 0
        book3 = 0
        result=[]
        predict_result = model.predict(userArr_n)
        print(predict_result)
        
        for i in range(3):
            ai_answer = np.argmax(predict_result)
            result.append(ai_answer)
            predict_result[0][ai_answer] = -1
        print(result)
        book1= str(result[0])
        book2= str(result[1])
        book3= str(result[2])
        print(book1,book2,book3)
        
        return book1, book2, book3
    
    
    
    
    
    
    # 0 : 호러, 1:코믹, 2:유머
    arr = [
            []
        ]