def seven_boom(end_number):
    """
    check if the numbers are BOOM (if a number is a severn multiplication or in a seven in it)
    :param end_number: the final number to check the BOOM
    :type end_number: int
    :return: list with the BOOM in the right places
    :rtype: list
    """

    new_list = list()

    # go over all the numbers enter them in to the new list and if it is a BOOM it a BOOM
    for i in range(0, end_number + 1):
        if '7' in str(i) or i % 7 == 0:
            new_list.append("BOOM")
        else:
            new_list.append(i)

    return new_list


def main():
    print(seven_boom(17))


if __name__ == "__main__":
    main()
