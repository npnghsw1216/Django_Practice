# 문자열을 인자로 받아, 단어수를 반환하는 함수를 작성하세요.


def get_word_count(s):
    return len(s.split())


print(get_word_count("우리는 파이썬을 즐겨요"))
