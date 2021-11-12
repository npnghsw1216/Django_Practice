import requests
from bs4 import BeautifulSoup


def check_available(received_text: str) -> bool:
    return received_text == "로또번호 조회"


def make_response(received_text: str, html: str = None) -> str:
    if html is None:
        url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%A1%9C%EB%98%90%EB%B2%88%ED%98%B8+%EB%8B%B9%EC%B2%A8%EB%B2%88%ED%98%B8+%EC%A1%B0%ED%9A%8C&oquery=%EB%A1%9C%EB%98%90%EB%B2%88%ED%98%B8&tqi=hh3pkdprvTossMF857sssssstpl-495514'
        response = requests.get(url)
        html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    title = soup.select_one("._lotto-btn-current").text

    tag_list = soup.select(".lotto_wrap .num_box .num")
    *numbers, bonus = [tag.text for tag in tag_list]
    message = f"""{title}
로또 번호: {", ".join(numbers)}
보너스 번호: {bonus}"""

    return message