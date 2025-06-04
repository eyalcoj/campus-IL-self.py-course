def extend_list_x(list_x, list_y):
    """
    the method is extend the first list (list x) when the second one is the first in order
    :param list_x: the list will add the other list
    :param list_y: the other list
    :type list_x: list
    :type list_y: list
    :return: it return the first new list (list x)
    :rtype: list
    """
    temp_list_y = list_y
    list_x, list_y = list_y, list_x
    list_x.extend(list_y)
    list_y = temp_list_y
    return list_x


def main():
    x = [4, 5, 6]
    y = [1, 2, 3]
    print(str(extend_list_x(x, y)))


if __name__ == "__main__":
    main()
