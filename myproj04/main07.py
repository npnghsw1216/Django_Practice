import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
song_list

for song in song_list:
    if song["artist"] == "방탄소년단":
        print(song["title"])
