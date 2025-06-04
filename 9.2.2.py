def copy_file_content(source, destination):
    """
    the function copies the contents of the source file to the destination file.
    :param source: the source file add
    :param destination: the destination file add
    :type source: str
    :type destination: str
    :return: nothing
    :rtype: None
    """

    with open(source) as fr, open(destination, "w") as fw:
        fw.write(fr.read())


def main():
    copy_file_content(r"C:\Users\Eyal\PycharmProjects\campus-IL-self.py-course\file1",
                      r"C:\Users\Eyal\PycharmProjects\campus-IL-self.py-course\file2")


if __name__ == "__main__":
    main()
