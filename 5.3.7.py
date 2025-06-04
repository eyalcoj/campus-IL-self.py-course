BIG = 5
SMALL = 1


def chocolate_maker(small, big, x):
    updated_x = -1
    if x // 5 <= big:
        updated_x = x % BIG
    else:
        updated_x - big * BIG
    return small >= updated_x


print(chocolate_maker(3, 1, 8))

print(chocolate_maker(3, 1, 9))

print(chocolate_maker(3, 2, 10))
