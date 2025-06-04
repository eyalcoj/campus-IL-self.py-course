def are_lists_equal(list1: list, list2: list):
    """
    check if the two list are equal but with a twist, it means that it can be in whatever order.
    :param list1: the first list
    :param list2: the second list
    :type list1: list
    :type list2:list
    :return: if those list are equal by the value of the lists
    :rtype: bool
    """
    list1.sort()
    list2.sort()
    return list1 == list2


def main():
    list1 = [0.6, 1, 2, 3]
    list2 = [3, 2, 0.6, 1]
    list3 = [9, 0, 5, 10.5]
    print(str(are_lists_equal(list1, list2)))
    print(str(are_lists_equal(list1, list3)))


if __name__ == "__main__":
    main()
