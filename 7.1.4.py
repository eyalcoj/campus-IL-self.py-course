def squared_numbers(start, stop):
    """
    this function calculate the power of the numbers from the start value to the end value. and insert them in to the arr
    :param start: the start number to start form to calculate the power
    :param stop:  the last number to stop the calculate the power
    :type start: int
    :type stop: int
    :return: the new list of all the power numbers
    :rtype: list
    """
    the_power_list = list()
    i = start
    # the calculate loop
    while i <= stop:
        the_power_list.append(i ** 2)
        i = i + 1

    return the_power_list


def main():
    print(squared_numbers(4, 8))
    print(squared_numbers(-3, 3))


if __name__ == "__main__":
    main()
