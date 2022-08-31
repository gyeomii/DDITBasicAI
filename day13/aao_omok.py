import numpy as np
from tensorboard.compat import tf
from keras.utils import to_categorical

class AaoOmok:
    def __init__(self):
        self.model = tf.keras.models.load_model('alphao2.h5')
    def mypredict(self,arr2D,flagWb):
        myarr2D =  arr2D.copy()
        myarr2D_n = np.array(myarr2D)
        if flagWb :
            for i in range(20):
                for j in range(20):
                    if myarr2D_n[i][j] == 2:
                        myarr2D_n[i][j] = -1
        else:
            for i in range(20):
                for j in range(20):
                    if myarr2D_n[i][j] == 1:
                        myarr2D_n[i][j] = -1
                    elif myarr2D_n[i][j] == 2:
                        myarr2D_n[i][j] = 1
        
        train_images = np.reshape(myarr2D_n,(1,400))
        predict_result = self.model.predict(train_images)
        
        for i in range(20):
            for j in range(20):
                if myarr2D[i][j] > 0 :
                    predict_result[0][i*20+j] = 0

        print("predict_result",predict_result[0])
                
        myargmax = np.argmax(predict_result[0])
        ii = int(myargmax/20)
        jj = myargmax % 20
        return ii,jj
        
            
if __name__ == '__main__':
    arr2D = [
        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
        
        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
        
        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
        
        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0]
    ]
    ao = AaoOmok()
    i,j = ao.mypredict(arr2D,True)
    print(i,j)
    
    
    
