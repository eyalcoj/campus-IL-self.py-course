def numbers_letters_count(my_str):
    """
    this function count the about of numbers in the str and the about of char
    :param my_str: the string witch is go to be counted
    :type my_str: str
    :return: list with the first is the number about and the second is the char amount
    :rtype: list
    """

    counter_numbers = 0
    counter_letters = 0

    # go over the string and count the letters and the numbers
    for char in my_str:
        if char.isdigit():
            counter_numbers = counter_numbers + 1
        else:
            counter_letters = counter_letters + 1

    return [counter_numbers, counter_letters]


def main():
    print(numbers_letters_count("Python 3.6.3"))


if __name__ == "__main__":
    main()
