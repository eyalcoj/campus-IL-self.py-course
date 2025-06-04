def arrow(my_char, max_length):
    """
    make un arrow witch in the widest point of it has the max_length from the char
    :param my_char: the char will be creating the arrow with
    :param max_length: the max length
    :type my_char: str
    :type max_length int
    :return: the arrow
    :rtype: str
    """

    counter_char = 1
    is_up = True
    the_char_list = list()

    while counter_char != 0:
        the_char_list.append(f"{my_char}" * counter_char)

        if is_up:
            counter_char += 1
            is_up = counter_char < max_length
        else:
            counter_char -= 1

    return '\n'.join(the_char_list)


def main():
    print(arrow('*', 5))


if __name__ == "__main__":
    main()
