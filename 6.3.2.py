def longest(my_list: list):
    """
    the method is finding the longest string value in the list and return it
    :param my_list:
    :type my_list:
    :return: the longest string in the list
    :rtype: string
    """

    my_list.sort(key=len)
    return my_list[-1]


def main():
    list1 = ["111", "234", "2000", "goru", "birthday", "09"]
    print(longest(list1))


if __name__ == "__main__":
    main()

