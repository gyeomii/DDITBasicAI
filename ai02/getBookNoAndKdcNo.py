import cx_Oracle
#한글 지원 방법
import os
import numpy as np
# 유저가 읽은 책의 KDC번호를 가져오는 클래스...?
class getBookNo:
    def __init__(self):
        os.putenv('NLS_LANG', '.UTF8')
        
        #연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
        dsn =cx_Oracle.makedsn('112.220.114.130','1521','xe')
        self.con = cx_Oracle.connect(user="team4_202204F",password="java",dsn=dsn,encoding="UTF-8")
        self.cursor = self.con.cursor()
        
    def selectBookNoOfMember(self, mem_id):
        sql1=f""" select book_no from rent_back where mem_id = '{mem_id}'
        """
        self.cursor.execute(sql1)
        row1 = self.cursor.fetchall()
        
        bookNoArr = []
        kdcNoArr = []
        kdcToZero = [0,0,0,0,0]
        kdcResult = [0,0,0,0,0]
        kdcResult10 = [0,0,1,0,2,  0,3,0,4,0]
        for idx, i in enumerate(row1) :
            bookNoArr.append(i[0]) # 해당하는 member가 읽은 책들의 no 배열 생성
            print(bookNoArr, "bookNoArrrrr")
            # 책번호 배열의 i번째 책에 해당하는 kdcNo 값 가져와서 kdcNoArr배열에 담음
            
        for i in bookNoArr:
            sql2 = f"select kdc_no from book where book_no = {i}"
            self.cursor.execute(sql2)
            row2 = self.cursor.fetchone()
            kdcNoArr.append(row2[0])
                
        print(row1, "row1")
        print(row2, "row2")
        print(bookNoArr, "bookNoArr")
        print(kdcNoArr,"kdcNoArr")
               
        
        for idx ,k in enumerate(kdcNoArr):
            print(idx)
            if kdcNoArr[idx] < 300 :
                kdcToZero[0] += 1
                if kdcToZero[0] > 0 and kdcToZero[0] < 4:
                    kdcResult10[1] = 1
                elif kdcToZero[0] > 3:
                    kdcResult10[1] = 2
                    
            elif kdcNoArr[idx] >=300 and kdcNoArr[idx] < 600: 
                kdcToZero[1] += 1
                if kdcToZero[1] > 0 and kdcToZero[1] < 4:
                    kdcResult10[3] = 1
                elif kdcToZero[1] > 3:
                    kdcResult10[3] = 2
                    
            elif kdcNoArr[idx] >=600 and kdcNoArr[idx] < 700:
                kdcToZero[2] += 1
                if kdcToZero[2] > 0 and kdcToZero[2] < 4:
                    kdcResult10[5] = 1
                elif kdcToZero[2] > 3:
                    kdcResult[5] = 2
                    
            elif kdcNoArr[idx] >=700 and kdcNoArr[idx] < 900:
                kdcToZero[3] += 1
                if kdcToZero[3] > 0 and kdcToZero[3] < 4:
                    kdcResult10[7] = 1
                elif kdcToZero[3] > 3:
                    kdcResult10[7] = 2
                    
            elif kdcNoArr[idx] >= 900 and kdcNoArr[idx] <1000:
                kdcToZero[4] += 1 
                if kdcToZero[4] > 0 and kdcToZero[4] < 4:
                    kdcResult10[9] = 1
                elif kdcToZero[4] > 3:
                    kdcResult10[9] = 2
                
        # print(kdcToZero)
        # print(kdcResult, "각 KDC에 해당하는 책마다 읽은 횟수를 반영한 결과")
        return kdcResult10
    
    
    # def selectCountBookNoOfMember(self, mem_id):
    #     sql=f"select count(*) from rent where mem_id = '{mem_id}'"
    #     self.cursor.execute(sql)
    #     row = self.cursor.fetchall()
    #     return row
    


    def __del__(self):
        self.cursor.close()
        self.con.close()

if __name__ == '__main__':
    # userArr = np.zeros(16)
    # bookLabel = []
    dao = getBookNo()
    row = dao.selectRmNO('aa')
    print(row);
    
    # kdcToZero = [0,0,0,0,0]
    # for idx ,k in enumerate(row):
    #     if row[idx] < 300 :
    #         kdcToZero[0] += 1
    #     elif row[idx] >=300 and row[idx] < 600:
    #         kdcToZero[1] += 1
    #     elif row[idx] >=600 and row[idx] < 700:
    #         kdcToZero[2] += 1
    #     elif row[idx] >=700 and row[idx] < 900:
    #         kdcToZero[3] += 1
    #     elif row[idx] >= 900 and row[idx] <1000:
    #         kdcToZero[4] += 1 
    #
    # print(kdcToZero)
    
    