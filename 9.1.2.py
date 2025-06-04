def main():

    path = input("please enter a path to text file: ")
    action = input("please enter an action (sort/rev/last): ")

    with open(path) as p:
        if action == "sort":
            word_list = p.read().replace("\n", " ").split(" ")
            word_list.sort()
            print(word_list)
        elif action == "rev":
            lines = p.readlines()
            for line in lines:
                print(line[::-1])
        elif action == "last":
            n = int(input("please enter number of lines to read: "))
            lines = p.readlines()
            for index in range(n):
                print(lines[index])
        else:
            print("error in the action input")


if __name__ == "__main__":
    main()
