# fmt : off


def mysum2(x, y):
    return x + y + 10


def mysum3(x, y, z):
    return x + y + z + 10


# 가변인자
def mysum(x, y, *args):
    # 인자가 없을 경우0개 이상으로 호출된다.
    # # args is tuple
    # x,y의 인자가 이미 있을경우 2개 이상으로 호출된다.
    print("args : ", args)
    return sum(args) + 10


print(mysum(1, 2))
print(mysum(1, 2, 3))
