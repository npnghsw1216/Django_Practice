def calculate_sum(max_number):
    accmulator = 0  # 누적할 변수
    for i in range(1, max_number + 1):
        accmulator += i
    return accmulator


print(calculate_sum(100))
