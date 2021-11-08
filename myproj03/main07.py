# 구구단 퀴즈 break 안 쓴 버전
# + 구구단 앞단의 범위에 대한 반복문 작성
# + 구구단 뒷단의 범위에 대한 반복문 작성 (범위를 number +1로 지정)
# + 구구단식을 출력문에 적어 출력
for number in range(2, 10):
    for i in range(1, number + 1):
        print(f"{number}*{i}={number*i}")
