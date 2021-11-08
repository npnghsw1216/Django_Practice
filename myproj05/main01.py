import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


# 1. 방탄소년단의 노래만 출력

for song_dict in song_list:
    if song_dict["artist"] == "방탄소년단":
        print(song_dict["title"])


# 2. "가을"이 들어가는 곡명만 출력

for song_dict in song_list:
    if "가을" == song_dict["title"]:
        print(song_dict["title"])

# 3. 좋아요 수가 200000이 넘는 곡수는?

song_count = 0

for song_dict in song_list:
    if song_dict["like"] == 200_000:
        song_count += 1
print(f"좋아요가 200,000이 넘는 곡은 {song_count}곡입니다.")

# 4. 가수 별 곡수를 출력해보세요.

artist_dict = {}
artist_list = []
for song_dict in song_list:
    artist: str = song_dict["artist"]  # type hint

    if artist not in artist_dict:
        artist_dict[artist] = 0
    artist_dict[artist] += 1

print(artist_dict)

{"방탄소년단": "값"}


artist_list = []

artist_list = [song_dict["artist"] for song_dict in song_list]
