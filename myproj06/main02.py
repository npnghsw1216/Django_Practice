import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

"""
멜론TOP100 리스트에서 "곡명" / 단어수의 리스트를 만들어봅시다.
- 총 100줄 중에 한 줄 출력 의 예 : Dynamite ➡ 1
"""

# for song_dict in song_list:
#     title : str = song_dict["title"]
#     title_length = len(title)
#     print(title, title_length)


def get_title_for_song(song_dict):
    return song_dict["title"]


# for song_dict in song_list:
#     print(get_title_for_song(song_dict))


# title_list = list(map(get_title_for_song, song_list))
# print(title_list)

# for title in map((get_title_for_song, song_list)):
#     print(f"{title} - {len(title)}")


# def get_title_and_length_for_song(song_dict):
#     title: str = song_dict["title"]
#     return [title, len(title)]


# for title, length in map(get_title_and_length_for_song, song_list):
#     print(title, length)

# 문제
# artist 글자수가 3글자 이상인 곡에 대해서
# 좋아요 수와 제목 글자수의 곱을 출력해보세요
# 1) for,if 로 구현

# check_lsit_3 = []
# check_like = []

# for song_dict in song_list:
#     if len(song_dict["artist"]) >= 3:
#         title: int = song_dict["title"]
#         like: int = song_dict["like"]
#         check_lsit_3.append([like, len(title)])
#         # for song_dict in song_list:
# #     title : str = song_dict["title"]
# #     title_length = len(title)
# #     print(title, title_length)

# for title, like in check_lsit_3:
#     print(f"{title}" title * like)


# 2) filter, map 위주로 구현
def check_bts_song(song_dict):
    return len(song_dict["artist"]) >= 3


def get_title_and_length_for_song(song_dict):
    title: str = song_dict["title"]
    like: int = song_dict["like"]
    return like * len(title)


for idx, like_length in enumerate(
    map(get_title_and_length_for_song, filter(check_bts_song, song_list))
):
    print("{title} {like_length}".format(like_length=like_length, **song_list[idx]))


# def check_letter_3(song_dict):
#     return song_dict["artist"] == "방탄소년단"


# for title, length in map(
#     get_title_and_length_for_song, filter(check_bts_song, song_list)
# ):
#     print(title, length)


# def check_letter_3(song_dict):
#     artist: int = song_dict["artist"]
#     return len(artist) >= 3


# for song_dict in filter(check_letter_3, song_list):
#     print("{like} * len{artist}".format(**song_dict))


# 방탄소년단의 노래에 대해서만, 곡명과 곡명의 글자수를 출력
# bts_list = []
# for song_dict in song_list:
#     if song_dict["artist"] == "방탄소년단":
#         title: str = song_dict["title"]
#         bts_list.append([title, len(title)])

# for title, length in bts_list:
#     print(title, length)

# # filter/map 버전
# def check_bts_song(song_dict):
#     return song_dict["artist"] == "방탄소년단"


# for title, length in map(
#     get_title_and_length_for_song, filter(check_bts_song, song_list)
# ):
#     print(title, length)


"""
멜론TOP100 리스트에서 "곡명" 단어수로 TOP10 곡명 출력
단어수가 제일 큰 노래가 우선순위가 가장 높겠죠.
"""
