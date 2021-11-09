# "곡명"단어수 TOP10

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


def pick_word_count_for_title(song_dict):
    # return song_dict["like"]
    title: str = song_dict["title"]
    word_list = title.split()
    return len(word_list)


sorted_song_list = sorted(song_list, key=pick_word_count_for_title, reverse=True)
top10_song_list = sorted_song_list[:10]

for song_dict in top10_song_list:
    print("{like} {title}".format(**song_dict))
