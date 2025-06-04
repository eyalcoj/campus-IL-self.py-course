def format_list(my_list: list):
    """
    the function takes the input list and manipulate it so will be with even index with ',' between and in last index with and before it
    :param my_list: the list with the values I going to look forward to, in ode length.
    :type my_list: list
    :return: the even index with ',' between and in last index with and before it.
    :rtype: list
    """
    ode_list = my_list[::2]
    last_index = my_list[-1]
    the_string = ', '.join(ode_list) + ", and " + str(last_index)

    return the_string


def main():
    print(str(format_list(["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"])))


if __name__ == "__main__":
    main()
