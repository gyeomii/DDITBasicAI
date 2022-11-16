from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import numpy as np

train_images_a =[
        [0,0],[0,0],[0,0],
        [0,1],[0,1],[0,1],
        [0,2],[0,2],[0,2],
        [1,0],[1,0],[1,0],
        [1,1],[1,1],[1,1],
        [1,2],[1,2],[1,2],
        [2,0],[2,0],[2,0],
        [2,1],[2,1],[2,1],
        [2,2],[2,2],[2,2],
        [3,0],[3,0],[3,0],
        [3,1],[3,1],[3,1],
        [3,2],[3,2],[3,2],
        [4,0],[4,0],[4,0],
        [4,1],[4,1],[4,1],
        [4,2],[4,2],[4,2],
        [5,0],[5,0],[5,0],
        [5,1],[5,1],[5,1],
        [5,2],[5,2],[5,2]
    ]

train_labels_a = [
    91,32,19,
    22,62,39,
    56,95,35,
    186,148,131,
    145,106,122,
    180,112,160,
    298,207,283,
    281,264,255,
    215,201,263,
    647,359,352,
    344,311,383,
    370,306,354,
    398,457,426,
    435,440,483,
    415,407,400,
    546,586,579,
    552,504,588,
    507,576,561

    ]
    

    

train_images = np.array(train_images_a)
print(train_images)
train_labels = np.array(train_labels_a)
print(train_labels.shape)

train_labels_c = to_categorical(train_labels, num_classes=648)
print("train_labels_c",train_labels_c)
print("len",train_labels_c[16])

model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(2,)))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(648, activation='softmax'))


model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])


model.fit(train_images, train_labels_c, epochs=200)

model.save("movieAI.h5");

predict_result = model.predict(train_images)


print("predict_result",predict_result)
for r in predict_result:
    ai_answer = np.argmax(r)
    print(ai_answer)
