# 최댓값을 구하는 방법
def get_max_number(number_list):
    number = number_list[0]  # index 참조
    for current_number in number_list:
        if current_number > number:
            number = current_number
    return number


def get_max_index(number_list):
    number = number_list[0]  # index 참조: 특정 값을 가져옴
    index = 0
    max_index = 0
    for index, current_number in enumerate(number_list):
        if current_number > number:
            number = current_number
            max_index = index
            index += 1
    return max_index


numbers = [17, 92, 18, 33, 58, 7, 33, 42]

print(get_max_number(numbers))
print(get_max_index(numbers))
