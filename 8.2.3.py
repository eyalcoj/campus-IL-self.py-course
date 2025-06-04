def mult_tuple(tuple1: tuple, tuple2: tuple):
    """
    calculate and return all the option for pers
    :param tuple1: the first tuple numbers
    :param tuple2: the second tuple numbers
    :type tuple1: tuple
    :type tuple2: tuple
    :return: all the option of the combination
    :rtype: tuple
    """

    list_of_all_couples = list()

    for index_val1 in tuple1:
        for index_val2 in tuple2:
            list_of_all_couples.append((index_val1, index_val2))
            list_of_all_couples.append((index_val2, index_val1))

    return tuple(list_of_all_couples)


def main():
    first_tuple = (1, 2, 3)
    second_tuple = (4, 5, 6)
    print(mult_tuple(first_tuple, second_tuple))


if __name__ == "__main__":
    main()
