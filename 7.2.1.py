def is_greater(my_list, n):
    """
    this method check if the every index if it bigger than and if it isn't remove it
    :param my_list: the list off all of the number to check
    :param n: the number witch is the minimum in the new list
    :type my_list: list
    :type n: int
    :return: the list with the number witch is bigger then n
    :rtype: list
    """

    # go over all of the value indexes, and remove all the values smaller than n
    new_list = list(my_list)
    for index_value in new_list:
        print(index_value)
        if index_value <= n:
            my_list.remove(index_value)

    return my_list


def main():
    result = is_greater([1, 30, 25, 60, 28, 27], 28)
    print(result)


if __name__ == "__main__":
    main()
