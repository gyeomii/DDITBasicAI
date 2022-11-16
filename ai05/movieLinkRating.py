import cx_Oracle
#한글 지원 방법
import os
import numpy as np
from ai05.naver2 import naverGet
class MOR:
    def __init__(self):
        os.putenv('NLS_LANG', '.UTF8')
        
        #연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
        dsn =cx_Oracle.makedsn('112.220.114.130','1521','xe')
        self.con = cx_Oracle.connect(user="team4_202204F",password="java",dsn=dsn,encoding="UTF-8")
        self.cursor = self.con.cursor()
        
    def selectMemberMOR(self,mono):
        sql=f"select mo_title from movie where mo_no = {mono}"
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        return row
    
    def selectMovieHistoryID(self,memId):
        sql=f"select mo_no from movie_history where mem_id = '{memId}'"
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        return row
    
    def selectMovieHistoryCount(self,memId):
        sql=f" select count(*) from movie_history where mem_id = '{memId}'"
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        return row
    
    def selectMovieHistory(self,memId):
        sql=f" select mo_no from movie_history where mem_id = '{memId}'"
        self.cursor.execute(sql)
        row = self.cursor.fetchall()
        return row

    def selectMovieGenre(self,mo_no):
        sql=f" select mo_genre from movie where mo_no = '{mo_no}'"
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        return row
    
    

#    def createDataSet(self):

    def updateMovieMOR(self,motitle, moimg, morating):
        sql=f"""update movie set mo_img = '{moimg}' ,  mo_rating = '{morating}' where mo_title = '{motitle}'
        """
        self.cursor.execute(sql)
        self.con.commit()
    
    def insertMoiveMOR(self,motitle,moimg,morating):
        sql=f"""insert into movie(mo_title, mo_img, mo_rating)
                values( '{motitle}', '{moimg}' ,  '{morating}')
        """
        
        self.cursor.execute(sql)
        self.con.commit()
        
    def __del__(self):
        self.cursor.close()
        self.con.close()

if __name__ == '__main__':
    dao = MOR()
    nave = naverGet()
    
    # 제목으로 insert 하기
    row = dao.selectMovieHistory('cc')
    genre0 = 0
    genre1 = 0
    genre2 = 0
    genre3 = 0
    genre4 = 0
    genre5 = 0
    
    for r in row:
        genre = dao.selectMovieGenre(r[0])[0]
        print(genre)
        if genre == 0:
            genre0 += 1
        elif genre == 1:
            genre1 += 1
        elif genre == 2:
            genre2 += 1
        elif genre == 3:
            genre3 += 1
        elif genre == 4:
            genre4 += 1
        elif genre == 5:
            genre5 += 1
    
    print(genre0, genre1,genre2,genre3, genre4,genre5)
    max = 0
    maxVal = 0
    if genre0 > max:
        max = genre0
        maxVal = 0
    elif genre1 > max:
        max = genre0
        maxVal = 1
    elif genre2 > max:
        max = genre1
        maxVal = 2
    elif genre3 > max:
        max = genre2
        maxVal = 3
    elif genre4 > max:
        max = genre3
        maxVal = 4
    elif genre5 > max:
        max = genre4
        maxVal = 5
        
    if max<2 :
        max = 0
    elif max>=2 and max <5 :
        max = 1
    elif max>=5 :
        max = 2
        
    userArr =[maxVal,max]
    print(userArr)
    # 제목 찾아와서 이미지 평점 넣기
    # nave = naverGet()
    # movie_list = []
    #
    #
    #
    # for i in range(440,601):
    #     row = dao.selectMemberMOR(i)
    #     movie_list = list(row)
    #     movei_name = movie_list[0]
    #     print(type(movei_name))
    # movei_name ='마녀'
    # image, rating = nave.getLinkRating(movei_name)
    # print(image)
    # print(rating)
    # dao.updateMovieMOR(movei_name, image, rating)

       
    
    
    