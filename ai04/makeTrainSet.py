import cx_Oracle
#한글 지원 방법
import os
import numpy as np
class Data:
    def __init__(self):
        os.putenv('NLS_LANG', '.UTF8')
        
        #연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
        dsn =cx_Oracle.makedsn('112.220.114.130','1521','xe')
        self.con = cx_Oracle.connect(user="team4_202204F",password="java",dsn=dsn,encoding="UTF-8")
        self.cursor = self.con.cursor()
        
    def selectTrainImage(self):
        sql=f"""select i, e, n, s, f, t, p, j
         from AI_MBTIBOOK"""
        self.cursor.execute(sql)
        row = self.cursor.fetchall()
        return row
    
    def selectTrainLabel(self):
        sql=f"""select book_no 
         from AI_MBTIBOOK"""
        self.cursor.execute(sql)
        row = self.cursor.fetchall()
        return row
    
#    def createDataSet(self):

    def __del__(self):
        self.cursor.close()
        self.con.close()

if __name__ == '__main__':
    userArr = np.zeros(8)
    print(userArr)
    trainLabel_a = []
    trainImage_a = []
    dao = Data()
    rows = dao.selectTrainImage()
    for row in rows:
        trainImage_a.append(list(row))
    trainImage = np.array(trainImage_a)
    print(trainImage[0])
    print(trainImage.shape)
    
    labels = dao.selectTrainLabel()
    for label in labels:
        trainLabel_a.append(label[0]-2557)
    trainLabel = np.array(trainLabel_a)
    print(trainLabel)
    print(trainLabel.shape)