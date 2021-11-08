import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# 정렬을 하려면, 각 값들에 대한 대소비교가 가능해야 한다.
# 10<100 '가'<'나
# {"A": 1} < {"B":2}  - 기준이 없어 대소 비교가 불가능하다


def 정렬기준값을_만들어줄_함수(song_dict):
    return song_dict["like"]


sorted_song_list = sorted(song_list, reverse=True, key=정렬기준값을_만들어줄_함수)

# for song_dict in sorted_song_list[0:10]:  top10

for song_dict in sorted_song_list:
    print("[{like}] {title} {artist}".format(**song_dict))
