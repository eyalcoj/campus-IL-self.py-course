def who_is_missing(file_name):
    """
    The file whose path is passed as an argument contains a list of integers from 1 to some n,
    unsorted, separated by commas, where one of the numbers in the sequence is missing.
    :param file_name: The function accepts as a parameter a path to a text file.
    :type file_name: str
    :return: the missing number
    :rtype: int
    """

    with open(file_name) as rf, open(r"C:\Users\Eyal\PycharmProjects\campus-IL-self.py-course\findMe.txt", "w") as wf:
        numbers = rf.read().split(',')
        for number in range(1, len(numbers) + 1):
            if str(number) not in numbers:
                wf.write(str(number))
                return number


def main():
    print(who_is_missing(r"C:\Users\Eyal\PycharmProjects\campus-IL-self.py-course\file2"))


if __name__ == "__main__":
    main()
