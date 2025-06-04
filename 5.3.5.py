def distance(num1, num2, num3):
    dnum12 = abs(num1 - num2)
    dnum13 = abs(num1 - num3)
    dnum23 = abs(num3 - num2)
    if (dnum12 <= 1 or dnum13 <= 1) and (dnum23 >= 2 and (dnum12 >= 2 or dnum13 >= 2)):
        return True
    else:
        return False



print(distance(1, 2, 10))
print(distance(4, 5, 3))
