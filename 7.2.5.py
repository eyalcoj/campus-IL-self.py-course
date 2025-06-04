from idlelib.debugobj import myrepr


def sequence_del(my_str):
    """
    this method remove all the recering strings
    :param my_str: the string I would check
    :type my_str: str
    :return: the new str without the recaring
    :rtype: str
    """

    the_char_index = 0
    the_new_str = str(my_str[the_char_index])

    for index in range(1, len(my_str)):
        if my_str[the_char_index] != my_str[index]:
            the_new_str += my_str[index]
            the_char_index = index

    return the_new_str


def main():
    print(sequence_del("ppyyyyythhhhhooonnnnn"))

    print(sequence_del("SSSSsssshhhh"))

    print(sequence_del("Heeyyy   yyyyyouuuu!!!"))


if __name__ == "__main__":
    main()
