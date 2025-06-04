def the_key(the_tuple: tuple):
    """
    this method return the price of the tuple
    :param the_tuple: represent a item with a price in the next formant ('item', 'price')
    :type the_tuple: tuple
    :return: the price
    :rtype: float
    """
    return the_tuple[1]


def sort_prices(list_of_tuples: list):
    """
    sort the list by the price.
    :param list_of_tuples: list of item represented by tuple, in the next format [('item', 'price'), ('item', 'price')]
    :type list_of_tuples: list of tuple
    :return: sortedlist by the price
    :rtype: list of tuple
    """

    list_of_tuples.sort(key=the_key)
    return list_of_tuples


def main():
    products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
    print(sort_prices(products))


if __name__ == "__main__":
    main()
