import requests

from bs4 import BeautifulSoup

def check_available(received_text: str) -> bool:
    return received_text.startswith("다음 검색:")

def make_response(received_text: str) -> str:
    q = received_text[6:]
    post_list = daum_search(q)

    response_text = "\n".join([post["title"] for post in post_list])
    return response_text

def daum_search(q):
    daum_search_url = "https://search.daum.net/search"
    params = {
        "w": "tot",
        "DA": "YZR",
        "t__nil_searchbox": "btn",
        "sug": "",
        "sugo": "",
        "sq": "",
        "o": "",
        "q": "q",
    }
    res = requests.get(daum_search_url, params=params)
    soup = BeautifulSoup(res.text, "html.parser")
    return [{"title": tag.text} for tag in soup.select(".lst_total .total_tit")]