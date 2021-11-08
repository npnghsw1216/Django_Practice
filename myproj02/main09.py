import random
import time

animal_names = [
    "cat",
    "dog",
    "fox",
    "monkey",
    "mouse",
    "panda",
    "frog",
    "snake",
    "wolf",
]

input("준비되셨으면, 엔터키를 입력해주세요.")

random.shuffle(animal_names)

begin_time = time.time()

ok_counter = 0

text_counter = 0

animal_count = len("{random_name}")

for random_name in animal_names[0:5]:

    # for count in range(5):
    #     random_name = random.choice(animal_names)
    # 방법1 : 이미 상용된 random_name을 받았다면 다시자겨오는 것
    text_counter += len(random_name)
    print(random_name)
    line = input(">>> ")
    if random_name == line:
        ok_counter += 1
        print("정확합니다.")
    else:
        print("오타가 있습니다.")

end_time = time.time()

speed = (text_counter * 60) // end_time

print(f"{ok_counter}번 성공하셨습니다.")
print(f"총 {end_time - begin_time}초 걸리셨습니다.")
print(f"타자속도 : {speed} 입니다.")
# (타수*60)/걸리 시간(초)
