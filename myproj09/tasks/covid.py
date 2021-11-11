import requests

from bs4 import BeautifulSoup

def check_available(received_text: str) -> bool:
    return received_text.startswith("코로나:")

def make_response(received_text: str) -> str:
    query = received_text[4:]
    covid_list = covid(query)

    response_text = "\n".join([post["title"] for post in covid_list])
    return response_text

def covid(코로나):
    search_url = "https://search.naver.com/search.naver"
    params = {
        "where": "nexearch",
        "sm": "tab_jum",
        "query": "코로나",  # 검색어
    }
    res = requests.get(search_url, params=params)
    soup = BeautifulSoup(res.text, "html.parser")
    return [{"title": tag.text} for tag in soup.select(".lst_total .total_tit")]