import cx_Oracle
#한글 지원 방법
import os
import numpy as np
class MBTI2:
    def __init__(self):
        os.putenv('NLS_LANG', '.UTF8')
        
        #연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
        dsn =cx_Oracle.makedsn('112.220.114.130','1521','xe')
        self.con = cx_Oracle.connect(user="team4_202204F",password="java",dsn=dsn,encoding="UTF-8")
        self.cursor = self.con.cursor()
        
    def selectMemberMBTI(self, mem_id):
        sql=f"select mem_mbti from member where mem_id = '{mem_id}'"
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        return row

#    def createDataSet(self):

    def __del__(self):
        self.cursor.close()
        self.con.close()

if __name__ == '__main__':
    mbtiMVArr = np.zeros(8)
    mvLabel = []
    
    dao = MBTI2()
    row = dao.selectMemberMBTI('aa')
    
    print(row[0])
    
    # if age <20:
    #     userArr[0] = 1
    # elif age >= 20 and age < 30:
    #     userArr[1] = 1
    # elif age >= 30 and age < 40:
    #     userArr[2] = 1
    # elif age >= 40 and age < 50:
    #     userArr[3] = 1
    # elif age >= 50:
    #     userArr[4] = 1
    #
    # if gender == 'M':
    #     userArr[5] = 1
    # elif gender == 'F':
    #     userArr[6] = 1
    #
    # userArr[int(inter1) + 6] = 1
    #
    # print(userArr)
    

    