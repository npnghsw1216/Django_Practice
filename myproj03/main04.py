""""""
# 반복문을 활용하여, 효과적으로 3단/6단/9단 구구단 출력하기
# + 구구단 앞단의 범위를 정해 3부터 시작하여 3씩 더하며 10 이하의 숫자에서 끝나게 범위 지정'
# + 구구단 뒷단의 범위를 정해 1부터 9 까지 순차적으로 계산하여 프린트 문을 만나 구현
for number in range(3, 10, 3):
    for i in range(1, 10):
        print(f"{number}*{i}={number*i}")
