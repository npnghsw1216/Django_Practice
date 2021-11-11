# 설치 : pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup


def naver_search(query):
    naver_search_url = "https://search.naver.com/search.naver"
    params = {
        "where": "view",
        "sm": "tab_jum",
        "query": query,  # 검색어
    }
    res = requests.get(naver_search_url, params=params)
    soup = BeautifulSoup(res.text, "html.parser")
    return [tag.text for tag in soup.select(".lst_total .total_tit")]


