import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# 좋아요수가 가장 많은곡은? 가장 적은곡은?


def peek_like_for_song(song_dict):
    return song_dict["like"]

# 1
song_dict = max(song_list, key=peek_like_for_song, default=None)
if song_dict == None:
    print("노래목록이 비었습니다.")
print(song_dict)

# 2
try:
    song_dict = max(song_list, key=peek_like_for_song, default=None)
except ValueError :
    print("노래목록이 비었습니다.")
else:
    print(song_dict)
# 3
if song_list:
    song_dict = max(song_list, key=peek_like_for_song)
    print(song_dict)
else:
    print("노래목록이 비었습니다.")