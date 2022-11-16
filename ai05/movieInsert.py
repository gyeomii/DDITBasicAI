import cx_Oracle
#한글 지원 방법
import os
import numpy as np
import requests
import json
import pandas as pd

class IM:
    def __init__(self):
        os.putenv('NLS_LANG', '.UTF8')
        
        #연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
        dsn =cx_Oracle.makedsn('112.220.114.130','1521','xe')
        self.con = cx_Oracle.connect(user="team4_202204F",password="java",dsn=dsn,encoding="UTF-8")
        self.cursor = self.con.cursor()
    
    def getMo_no(self):
        sql = "select mo_no_seq.nextval from dual"
        self.cursor.execute(sql)
        mo_no = self.cursor.fetchone()
        return int(mo_no[0])
    
    
    def insertMovie(self, mo_no, mo_genre, mo_title):
        sql=f"""INSERT INTO movie (mo_no, mo_genre, mo_title)
                 VALUES ( {mo_no}, {mo_genre}, '{mo_title}')"""
        print(sql)
        cnt = self.cursor.execute(sql)
        self.con.commit()
        return cnt

#    def createDataSet(self):

    def __del__(self):
        self.cursor.close()
       
        self.con.close()

if __name__ == '__main__':
    dao = IM()
    cnt = 1
    i = 4
    for x in range(1000):
        url = f"http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=da2d16002df0131bbea831f9d5e2482f&curPage={i}&itemPerPage=100&openStartDt=2010"
        res = requests.get(url)
        text= res.text
        
        d = json.loads(text)
        
        movie_list = []
        
        for b in d['movieListResult']['movieList']:
            if b['repGenreNm'] == 'SF':
                movie_list.append([b['movieCd'],b['movieNm'],b['repGenreNm']])
        
        print(movie_list)
        for movie in movie_list:
            mo_no = dao.getMo_no()
            mo_genre = 10
            if movie[2] == '애니메이션':
                mo_genre = 0
            elif movie[2] == '공포(호러)':
                mo_genre = 1
            elif movie[2] == '다큐멘터리':
                mo_genre = 2
            elif movie[2] == '코미디':
                mo_genre = 3
            elif movie[2] == '액션':
                mo_genre = 4
            elif movie[2] == 'SF':
                mo_genre = 5
            
            print(mo_genre, movie[1])
            dao.insertMovie(mo_no, mo_genre, movie[1])
            cnt += 1
            if cnt == 100:
                break
        if cnt == 100:
            break    
        i += 1