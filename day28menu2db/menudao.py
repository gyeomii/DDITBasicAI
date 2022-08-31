import pymysql
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import numpy as np
class MenuDao:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3305,
                       user='root', password='python',
                       db='python', charset='utf8')
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def getGroupMenu(self):
        sql = f"""
                SELECT distinct menu 
                FROM menu 
                ORDER BY menu   
            """
            
        arr = []
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        for row in rows:
            arr.append(row['menu'])
        return arr
    
    def getMenu(self, e_id):
        sql = f"""
                SELECT *
                FROM menu 
                WHERE e_id = '{e_id}'
                ORDER BY ymd  
            """
        arr = []
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        for row in rows:
            arr.append(row['menu'])
        return arr
    
    def myIdx(self,labels, menu):
        for idx, label in enumerate(labels):
            if(label == menu):
                return idx
    
    def labeling(self, labels, menus):
        arr=[]
        for menu in menus:
            idx = self.myIdx(labels, menu);
            arr.append(idx)
        return arr
    
    
    def makeDataSet(self, menuList):
        train_data=[]
        train_label=[]
        for i in range(len(menuList)-2):
            list=[]
            list.append(menuList[i])
            list.append(menuList[i+1])
            train_data.append(list)
            
            train_label.append(menuList[i+2])
        return train_data,train_label
    
    def makeH5(self, train_data_n, train_label_n):
        
        train_labels_c = to_categorical(train_label_n, num_classes=len(labels)) 
        print("train_labels_c",train_labels_c)
        
        model = models.Sequential()
        model.add(layers.Dense(1024, activation='relu', input_shape=(2,)))
        model.add(layers.Dense(1024, activation='relu'))
        model.add(layers.Dense(2048, activation='relu'))
        model.add(layers.Dense(2048, activation='relu'))
        model.add(layers.Dense(11, activation='softmax'))
        
        model.compile(optimizer='rmsprop',
                        loss='categorical_crossentropy',
                        metrics=['accuracy'])
        
        model.fit(train_data_n, train_labels_c, epochs=150)
        
        model.save("2.h5");
        predict_result = model.predict(train_data_n)
        print(predict_result)
        for r in predict_result:
            ai_answer = np.argmax(r)
            print(ai_answer,end=",")
        print()
        
    def __del__(self):
        # self.cur.close()
        # self.conn.close()
        pass
        
if __name__ == '__main__':
    dao = MenuDao()
    labels = dao.getGroupMenu()
    menus = dao.getMenu(2)
    menuList = dao.labeling(labels, menus)
    train_data, train_label = dao.makeDataSet(menuList)
    train_data_n = np.array(train_data) / (len(labels)-1)
    train_label_n = np.array(train_label)
    dao.makeH5(train_data_n,train_label_n)
    
    print("labels", labels)
    print("menus", menus)
    print("menuList", menuList)
    print("train_data",train_data)
    print("train_label", train_label)
    print("train_data_n",train_data_n)
    print("train_label_n", train_label_n)
    
    