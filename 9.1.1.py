def are_files_equal(file1, file2):
    """
    check if the file content is the same
    :param file1: first file
    :param file2: second file
    :type file1: str
    :type file2: str
    :return: if the file are having the same content
    :rtype: bool
    """
    with open(file1) as f_file, open(file2) as s_file:
        return f_file.read() == s_file.read()


def main():
    print(are_files_equal(r"C:\Users\Eyal\PycharmProjects\campus-IL-self.py-course\file1",
                          r"C:\Users\Eyal\PycharmProjects\campus-IL-self.py-course\file2"))


if __name__ == "__main__":
    main()
