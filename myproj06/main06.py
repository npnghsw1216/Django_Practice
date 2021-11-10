# 좋아요 수로 TOP10 곡명 리스트를 만들오 봅시다.

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


def pick_like_value(song_dict):
    return song_dict["like"]


sorted_song_list = sorted(song_list, key=pick_like_value, reverse=True)
top10_song_list = sorted_song_list[:10]

for song_dict in top10_song_list:
    print("{like} {title}".format(**song_dict))
