# a="우리는 파이썬을 즐겨요"
# b=a.replace(" ","")
# print(len(b))


# def remove_space(a):
#     return len(a.replace(" ", ""))


# print(remove_space("우리는 파이썬을 즐겨요"))
# print(remove_space("박 박 박 박 박 박"))


# def remove_space(a):
#     return a.strip()


# print(remove_space(" 우리는 "))
# print(remove_space("         우리는           "))

# a = 1234567
# b = int(a / 1000) * 1000
# print(b)


def number_return(a):
    return int(a / 1000) * 1000


print(number_return(1234567))
print(number_return(9876543))
