# 랜덤 숫자를 맞춰보세요.
# hint: random.randint를 통해 1이상 100이하의 랜덤수를 만듭니다.
# 유저에게 10회의 기회를 줍니다.- for/range
#  그 숫자를 정확히 맞췄다면, 몇 번 만에 맞췄는 지 출력
#  입력한 숫자가 랜덤수보다 작다면, "더 큰 수를 입력해주세요." 라고 출력
#  입력한 숫자가 랜덤수보다 크다면, "더 작은 수를 입력해주세요."라고 출력
#  횟수를 초과했다면, "다음 기회에 ..."
import random

random_number = random.randint(1, 100)
number_count = 1
for i in range(10):
    input_number = input("1~100 숫자를 입력하세요: ")
    input_number = int(input_number)
    if random_number == input_number:
        print(f"{number_count}번만에 맞췄습니다")
        break
    elif 100 >= input_number > random_number:
        number_count += 1
        if number_count == 11:
            break
        else:
            print("랜덤수보다 작은 수를 입력해주세요")
    elif 1 <= input_number < random_number:
        number_count += 1
        if number_count == 11:
            break
        else:
            print("랜덤수보다 큰 수를 입력해주세요")
    elif input_number < 1 or input_number > 100:
        number_count += 1
        if number_count == 11:
            break
        else:
            print("범위에 맞지 않는 수를 입력하였습니다")
if number_count == 11:
    print("다음 기회에..")
