import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


"""
for song_dict in song_list:
    if song_dict["artist"] == "방탄소년단":
        print(song_dict["title"])
"""
"""
def 정렬기준값을_만들어줄_함수(song_dict):
    return song_dict["like"]


sorted_song_list = sorted(song_list, reverse=True, key=정렬기준값을_만들어줄_함수)

# for song_dict in sorted_song_list[0:10]:  top10

for song_dict in sorted_song_list:
    print("[{like}] {title} {artist}".format(**song_dict))
"""


def fn_1(song_dict):
    return len(song_dict["title"].split(" "))


sorted_song_list = sorted(song_list, reverse=True, key=fn_1)

for song_dict in sorted_song_list:

    print("[{title}] -> ".format(**song_dict))
