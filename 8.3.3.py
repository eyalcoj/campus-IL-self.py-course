def count_chars(my_str: str):
    """
    this program organize this str in to a dire by the letters
    :param my_str: the str to brake down
    :type my_str: str
    :return: the letters as a key and the number of times my the value
    :rtype: dir
    """

    the_final_dir = dict()
    for index_val in my_str.replace(" ", ""):
        if index_val in the_final_dir.keys():
            the_final_dir[index_val] += 1
        else:
            the_final_dir[index_val] = 1

    return the_final_dir


def main():
    magic_str = "abra cadabra"
    print(count_chars(magic_str))


if __name__ == "__main__":
    main()
