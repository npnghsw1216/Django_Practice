from typing import List
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

new_song_list : List[dict] = []
for song_dict in song_list:
    artist : str = song_dict["artist"]
    if len(artist) >= 3:
        value : int =song_dict["like"] * len(song_dict["title"])
        new_song_list.append(dict(song_dict, value = value))
    #     new_song_list.append(
    #         {
    #         "title" : song_dict["title"]
    #         "artist" : song_dict["artist"]
    #         "like" : song_dict["like"]
    #         "album" : song_dict["album"]
    #         "rank" : song_dict["rank"]
    #         "value" : value.
    #     }
    # )

for value in value_list:
    print(value)