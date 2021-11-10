# 2곡 이상 랭크된 가수는 몇 팀인가요?

# from collections import defaultdict, Counter
# from pprint import pprint
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


# # 1

# artist_list = [song_dict["artist"] for song_dict in song_list]

# song_count_dict = {}  # key : artist, value : song count
# for artist in artist_list:
#     if artist not in song_count_dict:
#         song_count_dict[artist] = 0
#     song_count_dict[artist] += 1

# pprint(song_count_dict)

# 2

# song_count_dict = defaultdict(int)
# for artist in artist_list:
#     song_count_dict[artist] += 1

# pprint(song_count_dict)

#  3 : 나름 괜츈

# song_count_dict = Counter(artist_list)

# artist_count_above_2 = 0
# for song_counnt in song_count_dict.values():
#     if song_counnt >= 2:
#         artist_count_above_2 += 1

# pprint(artist_count_above_2)

# 4
song_count_dict = Counter(artist_list)


def check_above_1(song_count):
    return song_count > 1


print(len(list(filter(check_above_1, song_count_dict.values()))))
