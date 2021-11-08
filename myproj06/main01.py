from pprint import pprint
from typing import List
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


""""""


# title_list: List[str] = []

# for song_dict in song_list:
#     artist: str = song_dict["artist"]
#     if artist == "방탄소년단":
#         title: str = song_dict["title"]
#         title_list.append(title)

# print(title_list)


def check_bts_song(song_dict):
    """
    BTS 노래라면 True를 반환합니다.
    """

    # bts 노래라면 True를 리턴, 아니라면 False를 리턴
    artist: str = song_dict["artist"]
    return artist == "방탄소년단"


# new_song_list: List[dict] = []

# for song_dict in song_list:
#     if check_bts_song(song_dict):
#         new_song_list.append(song_dict)

# pprint(new_song_list)

new_song_list = list(filter(check_bts_song, song_list))
print(new_song_list)

# 단순히 print만 한다라고 한다면
for song_dict in filter(check_bts_song, song_list):
    print("{title} {artist} {like}".format(**song_dict))


""""""

print("------------------------------------------")


def check_contains_love(song_dict):
    title: str = song_dict["title"]
    return "사랑" in title


for song_dict in filter(check_contains_love, song_list):
    print("{rank} {title}".format(**song_dict))


# title_list: List[str] = []


# for song_dict in song_list:
#     title: str = song_dict["title"]
#     if "사랑" in title:
#         title_list.append(title)

# print(title_list)


""""""

print("-----------------------------------------")


def check_above_200000(song_dict):
    like: int = song_dict["like"]
    return like >= 200_000


for song_dict in filter(check_above_200000, song_list):
    print("{title} - {like}".format(**song_dict))


# title_list: List[str] = []
# for song_dict in song_list:
#     title: str = song_dict["title"]
#     like: int = song_dict["like"]
#     if like >= 200_000:
#         title_list.append(title)

# print(title_list)
