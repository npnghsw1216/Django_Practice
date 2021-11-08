""""""
# 1이상 100미만 범위에서 3과 5의 공배수를 합을 출력하기
# + 합을 구하는 변수 선언
# + 합의 값 0에 3과 5의 공배수가 나온 값 축적
# + 출력
""""""
sum = 0
for number in range(1, 100):
    if number % (3 * 5) == 0:
        sum += number
print(sum)
