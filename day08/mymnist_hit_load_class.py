
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import numpy as np

class HerKY:
    def __init__(self):
        self.model = tf.keras.models.load_model('mnist_hit.h5')
        
    def guess(self,train_images_a):
        # train_images_a = [[0]],[[0.5]],[[1]]
        train_images = np.array(train_images_a)
        predict_result = self.model.predict(train_images)
        ai_answer = np.argmax(predict_result[0])
        return ai_answer

        
if __name__ == '__main__':
    hky = HerKY()
    ans = hky.guess([[0,0,0,0,0    ,0,0,0,1]])
    print("ans",ans)