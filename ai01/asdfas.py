import requests
import json
import pandas as pd

url = 'http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=da2d16002df0131bbea831f9d5e2482f&curPage=1&itemPerPage=100&openStartDt=2020'
res = requests.get(url)
text= res.text

d = json.loads(text)

movie_list = []

for b in d['movieListResult']['movieList']:
    if b['repGenreNm'] == '멜로/로맨스':
        movie_list.append([b['movieCd'],b['movieNm'],b['repGenreNm']])

print(movie_list)
data = pd.DataFrame(movie_list)
print(data)
data.to_csv("movie_list.txt", mode='w', encoding='utf-8', index=False)