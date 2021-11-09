# 방탄소년단의 좋아요 총 합은??

# List Comprehension with if statement
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

like_sum_for_bts = sum(
    [song_dict["like"] for song_dict in song_list if song_dict["artist"] == "방탄소년단"]
)

print(like_sum_for_bts)
