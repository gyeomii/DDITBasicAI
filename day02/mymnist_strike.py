from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import numpy as np

case_all = []
case_ans = []
ti_as = []

for i in range(1,9+1):
    for j in range(1,9+1):
        case_all.append([i,j])
        if i == j :
            case_ans.append(1)
        else :
            case_ans.append(0)

print(case_all)        
        
for i in range(81):
    ti_a = []
    if  case_all[i][0] == 1:
        ti_a.append(1);ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);     ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);
    if  case_all[i][0] == 2:
        ti_a.append(0);ti_a.append(1);ti_a.append(0);ti_a.append(0);ti_a.append(0);     ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);
    if  case_all[i][0] == 3:
        ti_a.append(0);ti_a.append(0);ti_a.append(1);ti_a.append(0);ti_a.append(0);     ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);
        
    if  case_all[i][0] == 4:
        ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(1);ti_a.append(0);     ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);
    if  case_all[i][0] == 5:
        ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(1);     ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);
    if  case_all[i][0] == 6:
        ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);     ti_a.append(1);ti_a.append(0);ti_a.append(0);ti_a.append(0);
        
    if  case_all[i][0] == 7:
        ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);     ti_a.append(0);ti_a.append(1);ti_a.append(0);ti_a.append(0);
    if  case_all[i][0] == 8:
        ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);     ti_a.append(0);ti_a.append(0);ti_a.append(1);ti_a.append(0);
    if  case_all[i][0] == 9:
        ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);     ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(1);
        
    if  case_all[i][1] == 1:
        ti_a.append(1);ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);     ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);
    if  case_all[i][1] == 2:
        ti_a.append(0);ti_a.append(1);ti_a.append(0);ti_a.append(0);ti_a.append(0);     ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);
    if  case_all[i][1] == 3:
        ti_a.append(0);ti_a.append(0);ti_a.append(1);ti_a.append(0);ti_a.append(0);     ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);
        
    if  case_all[i][1] == 4:
        ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(1);ti_a.append(0);     ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);
    if  case_all[i][1] == 5:
        ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(1);     ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);
    if  case_all[i][1] == 6:
        ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);     ti_a.append(1);ti_a.append(0);ti_a.append(0);ti_a.append(0);
        
    if  case_all[i][1] == 7:
        ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);     ti_a.append(0);ti_a.append(1);ti_a.append(0);ti_a.append(0);
    if  case_all[i][1] == 8:
        ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);     ti_a.append(0);ti_a.append(0);ti_a.append(1);ti_a.append(0);
    if  case_all[i][1] == 9:
        ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(0);     ti_a.append(0);ti_a.append(0);ti_a.append(0);ti_a.append(1);
        
    ti_as.append(ti_a)
    
    
print(ti_as)    

train_images = np.array(ti_as)
train_labels = np.array(case_ans)

print("train_images",train_images)   
print("train_labels",train_labels)   


train_labels_c = to_categorical(train_labels)
print("train_labels_c",train_labels_c)

model = models.Sequential()
model.add(layers.Dense(1024, activation='relu', input_shape=(18,)))
model.add(layers.Dense(2, activation='softmax'))


model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])


model.fit(train_images, train_labels_c, epochs=20, batch_size=4)

predict_result = model.predict(train_images)
print("predict_result",predict_result)
for idx,r in enumerate(predict_result):
    print(idx,np.argmax(r))







