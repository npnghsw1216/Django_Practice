"""
멜론TOP100 리스트에서 "곡명" 단어수로 TOP10 곡명 출력
단어수가 제일 큰 노래가 우선순위가 가장 높겠죠
"""

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# 좋아요 수로 TOP10 곡명 리스트를 만들오 봅시다.
def pick_like_value(song_dict):
    return song_dict["like"]


sorted_song_list = sorted(song_list, key=pick_like_value, reverse=True)
top10_song_list = sorted_song_list[:10]

for song_dict in top10_song_list:
    print("{like} {title}".format(**song_dict))
