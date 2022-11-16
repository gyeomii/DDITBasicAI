import cx_Oracle
#한글 지원 방법
import os
import numpy as np
class celebBook:
    def __init__(self):
        os.putenv('NLS_LANG', '.UTF8')
        
        #연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
        dsn =cx_Oracle.makedsn('112.220.114.130','1521','xe')
        self.con = cx_Oracle.connect(user="team4_202204F",password="java",dsn=dsn,encoding="UTF-8")
        self.cursor = self.con.cursor()
        
    def selectCelebBook(self, celeb):
        sql=f"select book_no from ai_celeb where celeb = '{celeb}'"
        self.cursor.execute(sql)
        row = self.cursor.fetchall()
        return row

#    def createDataSet(self):

    def __del__(self):
        self.cursor.close()
        self.con.close()
if __name__ == '__main__':
    dao = celebBook()
    row = dao.selectCelebBook('공유')
    print(row[0][0]);