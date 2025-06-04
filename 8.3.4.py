def inverse_dict(my_dict: dict):
    """
    this function will is making the keys value and the value keys
    :param my_dict: the dict to inverse
    :type my_dict: dict
    :return: a new inverse dict
    :rtype: dict
    """
    new_dict = dict()

    # filter recurring values
    all_values = list(my_dict.values())
    unic_all_values = list()

    for value in all_values:
        if value not in unic_all_values:
            unic_all_values.append(value)

    for key in list(my_dict.keys()):
        if my_dict[key] in new_dict.keys():
            new_dict[my_dict[key]].append(key)
        else:
            new_dict[my_dict[key]] = [key]

    return new_dict


def main():
    course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
    print(inverse_dict(course_dict))


if __name__ == "__main__":
    main()
