s = "안녕하세요."

idx = 0
for ch in s:
    print(idx, ch)
    idx += 1

for idx, ch in enumerate(s, 1):
    print(idx, ch)

# ...
