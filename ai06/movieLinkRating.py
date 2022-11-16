import os

import cx_Oracle

#한글 지원 방법
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
        sql=f"select mh_no, mem_id, mo_no, mo_date from movie_history where mem_id = '{memId}'"
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        return row
    
    def selectMovieHistoryCount(self,memId):
        sql=f" select count(*) from movie_history A where mem_id = '{memId}'"
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
        
    def insertMovieName(self,mo_title,mo_genre):
        sql=f"""insert into movie(mo_no,mo_title,mo_genre)
                values (mo_no_seq.nextval,'{mo_title}','{mo_genre}')
                """
        self.cursor.execute(sql)
        self.con.commit()
        
        
    def __del__(self):
        self.cursor.close()
        self.con.close()
        
    
    
    