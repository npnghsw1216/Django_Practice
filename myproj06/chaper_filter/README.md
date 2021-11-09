# 내장함수 filter

from typing import List
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# 문제
# artist 글자수가 3글자 이상인 곡에 대해서
# 각 곡의 좋아요 수와 제목글자수의 곱을 출력해보세요.

# 1) for/if로 구현

new_song_list: List[dict] = []
for song_dict in song_list:
    artist: str = song_dict["artist"]
    if len(artist) >= 3:
        value: int = song_dict["like"] * len(song_dict["title"])
        new_song_list.append(dict(song_dict, value=value))
        # new_song_list.append(
        #     {
        #         "title": song_dict["title"],
        #         "artist": song_dict["artist"],
        #         "like": song_dict["like"],
        #         "album": song_dict["album"],
        #         "rank": song_dict["rank"],
        #         "value": value,
        #     }
        # )

for song_dict in new_song_list:
    print("{title} / {value}".format(**song_dict))


# 교육 7일차

## 파이썬 map

목록으로부터 값을 하나씩 받아서 변환하여, 새로운 목록을 생성

```python
def make_power(number):
    return number ** 2

for number in map(make_power, range(1, 10)):
    print(number)
```