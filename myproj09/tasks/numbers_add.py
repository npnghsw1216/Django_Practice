import re


def check_available(received_text: str) -> bool:
    return received_text.startswith("숫자더하기:")


def make_response(received_text: str) -> str:
    line = received_text[6:]
    # 1개 이상의 숫자 문자열로 구성된 문자열의 리스트를 생성
    calculated_number = sum(map(int, re.findall(r"\d+", line)))
    return str(calculated_number)