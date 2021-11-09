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


while True:
    line = input("Enter question (quit: q): ")
    if line == "q":
        print("안녕. 잘 가.")
        break
    # "네이버 검색: 파이썬"
    elif line.startswith("네이버 검색:"):
        query = line[7:]  # 검색어
        title_list = naver_search(query)
        print(f"=== 네이버 검색 결과 : {query} ===")
        for idx, title in enumerate(title_list, 1):
            print(f"[{idx}] {title}")
        print(title_list)
    elif line == "야":
        print("왜?")
    else:
        print("니가 무슨 말을 하는 지 모르겠어.")
