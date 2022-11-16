rapidapi_key = 'd2076dd318msh66e560f71e14780p1ce375jsn9f879a7425a2'
naver_client_id = 'LWMpre6WJGR7TwFHRs8D'
naver_client_secret = 'sNCw_xKc7p'

import requests
from pprint import pprint

#요약

url = "https://tldrthis.p.rapidapi.com/v1/model/abstractive/summarize-url/"

payload = {
    "url": "https://arxiv.org/pdf/1706.03762.pdf", # 주소
    "min_length": 100, # 최소 길이
    "max_length": 300, # 최대 길이
    "is_detailed": False # 한 문장으로 반환할 것인지 여부
}

headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": rapidapi_key,
    "X-RapidAPI-Host": "tldrthis.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

pprint(response.json())

summary = response.json()['summary'][0].strip()

print(summary)

#번역

url = "https://openapi.naver.com/v1/papago/n2mt"

payload = {

# 영어(en)로 받아서 한글(ko)로 추출
    "source": "en",   
    "target": "ko",
    "text": summary,
}

headers = {
    "content-type": "application/json",
    "X-Naver-Client-Id": naver_client_id,
    "X-Naver-Client-Secret": naver_client_secret,
}

response = requests.request("POST", url, json=payload, headers=headers)

pprint(response.json())


print(response.json()['message']['result']['translatedText'])

def summarize_and_translate(article_url, min_length=100, max_length=300):
    url = "https://tldrthis.p.rapidapi.com/v1/model/abstractive/summarize-url/"

    payload = {
        "url": article_url, # 주소
        "min_length": min_length, # 최소 길이
        "max_length": max_length, # 최대 길이
        "is_detailed": False # 한 문장으로 반환할 것인지 여부
    }

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": rapidapi_key,
        "X-RapidAPI-Host": "tldrthis.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    summary = response.json()['summary'][0].strip()
    
    url = "https://openapi.naver.com/v1/papago/n2mt"

    payload = {
        "source": "en",
        "target": "ko",
        "text": summary,
    }

    headers = {
        "content-type": "application/json",
        "X-Naver-Client-Id": naver_client_id,
        "X-Naver-Client-Secret": naver_client_secret
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    
    return response.json()['message']['result']['translatedText']

summarize_and_translate("https://arxiv.org/pdf/1706.03762.pdf", 50, 100)

summarize_and_translate("https://arxiv.org/pdf/1905.11946.pdf", 100, 200)