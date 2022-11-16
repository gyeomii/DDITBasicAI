import os
import sys
import requests

class naverGet:

    def getLinkRating(self,movieName):
    #네이버 영화 API 키 값
        client_id = "m9QEHepvmKGmUAfIVccc"
        client_secret = "4UBxVMUJ8P"
        
        
        movie = movieName
        header_parms ={"X-Naver-Client-Id":client_id,
                       "X-Naver-Client-Secret":client_secret}
        
        url = f"https://openapi.naver.com/v1/search/movie.json?query={movie}"
        res=requests.get(url,headers=header_parms)
        data =res.json()
        
        #데이터 전처리
        title=data['items'][0]['title'].strip('</b>')
        image=data['items'][0]['image']
        rating=float(data['items'][0]['userRating'])
        
        
        return image, rating