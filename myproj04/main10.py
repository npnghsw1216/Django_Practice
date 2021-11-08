import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
song_list


singer = []

for song in song_list:
    singer.append(song["artist"])

a = set(singer)

dic_dic = {}
for singer in a:
    count = 0
    for i in singer:
        if ch == i:
            count += 1
            dic_dic[a] = count
    print(dic_dic)
