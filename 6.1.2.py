def shift_left(my_list: list):
    """
    this function is shifting the list to the left
    :param my_list: the list to shift in length of 3
    :type my_list: list
    :return: the shift left of the list
    :rtype: list
    """
    my_list = [my_list[1], my_list[2], my_list[0]]
    return my_list


def main():
    print(shift_left(['monkey', 2.0, 1]))


if __name__ == "__main__":
    main()