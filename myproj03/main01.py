"""
* 1이상 40이하 범위에서 랜덤수를 획득하고
* 10 미만이라면 1을 출력하고
* 10 이상 20 미만이라면 10을 출력하고
* 20 이상 30 미만이라면 20을 출력하고
* 30 이상이라면, "너무 큰 수" 라고 출력합니다.
* 프로그램 종료 시에 "숫자는 ???입니다."라고 출력

"""
from random import randint

number = randint(1, 40)

if number < 10:
    print(1)
elif 10 <= number < 20:
    print(10)
elif 20 <= number < 30:
    print(20)
else:
    print("너무 큰 수")

print(f"숫자는{number}입니다.")
