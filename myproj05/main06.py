import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


def fn_1(song_dict):
    return len(song_dict["title"].split(" "))


sorted_song_list = sorted(song_list, reverse=True, key=fn_1)

for song_dict in sorted_song_list:

    print("[{title}] -> ".format(**song_dict))
