def main():
    the_list = input("please enter a list of products to shop: ")
    the_list_as_list = the_list.split(',')

    run = True

    while run:
        the_action_type = int(input("please give a action type (1 - 9): "))

        if the_action_type == 1:
            print(the_list)

        elif the_action_type == 2:
            print(len(the_list_as_list))

        elif the_action_type == 3:
            the_product = input("please enter a product and I will check if it is in the list: ")
            print(bool(the_list_as_list.count(the_product)))

        elif the_action_type == 4:
            the_product = input("please enter a product and I will who match is in the list: ")
            print(the_list_as_list.count(the_product))

        elif the_action_type == 5:
            the_product = input("please enter a product and I will remove it from the list: ")
            the_list_as_list.remove(the_product)
            the_list = ','.join(the_list_as_list)

        elif the_action_type == 6:
            the_product = input("please enter a product and I will add it from the list: ")
            the_list_as_list.append(the_product)
            the_list = ','.join(the_list_as_list)

        elif the_action_type == 7:
            for index in the_list_as_list:
                # Check if the values are valid
                if len(index) < 3 or not index.isalpha():
                    print(index)

        elif the_action_type == 8:
            for index in the_list_as_list:
                # Check if dupe
                count = the_list_as_list.count(index)
                for i in range(1, count):
                    the_list_as_list.remove(index)

            the_list = ','.join(the_list_as_list)

        elif the_action_type == 9:
            print("STOPPING")
            run = False


if __name__ == "__main__":
    main()
