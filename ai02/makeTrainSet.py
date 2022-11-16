import cx_Oracle
#한글 지원 방법
import os
import numpy as np
class DS:
    def __init__(self):
        os.putenv('NLS_LANG', '.UTF8')
        
        #연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
        dsn =cx_Oracle.makedsn('112.220.114.130','1521','xe')
        self.con = cx_Oracle.connect(user="team4_202204F",password="java",dsn=dsn,encoding="UTF-8")
        self.cursor = self.con.cursor()
        
    def selectTrainImage(self):
        sql=f"""select kdc100200, cnt1, kdc300_500, cnt2, kdc600, cnt3, kdc700800, cnt4, kdc900, cnt5
         from ai_kdcbook"""
        self.cursor.execute(sql)
        row = self.cursor.fetchall()
        return row
    
    def selectTrainLabel(self):
        sql=f"""select book_no 
         from ai_kdcbook"""
        self.cursor.execute(sql)
        row = self.cursor.fetchall()
        return row
    
#    def createDataSet(self):

    def __del__(self):
        self.cursor.close()
        self.con.close()

if __name__ == '__main__':
    kdcResult10 = [0,0,1,0,2,  0,3,0,4,0]
    trainLabel_a = []
    trainImage_a = []
    dao = DS()
    rows = dao.selectTrainImage()
    for row in rows:
        trainImage_a.append(list(row))
    trainImage = np.array(trainImage_a)
    print(trainImage[0])
    print(trainImage.shape)
    
    labels = dao.selectTrainLabel()
    for label in labels:
        trainLabel_a.append(label[0])
    trainLabel = np.array(trainLabel_a)
    print(trainLabel)
    print(trainLabel.shape)
    
    
    