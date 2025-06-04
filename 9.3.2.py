def my_mp4_playlist(file_path, new_song):
    """
    The function writes to the file the string representing the name of a new song (new_song)
    instead of the name of the song that appears in the third line of the file. and print the file.
    :param file_path: The file represents a playlist of songs and has a fixed format consisting of the song name,
    the artist name (singer/band) and the song length, separated by a semicolon (;) without spaces.
    :param new_song: A string representing the name of a new song
    :type file_path: str
    :type new_song: str
    :return: nothing
    :rtype: None
    """

    lines = list()
    with open(file_path) as rf:
        lines = rf.readlines()

        for i_line in range(len(lines)):
            lines[i_line] = lines[i_line].split(";")

        lines[2][0] = new_song

    with open(file_path, "w") as wf:
        for i_line in range(len(lines)):
            lines[i_line] = ';'.join(lines[i_line])

        wf.writelines(lines)

    with open(file_path) as rf:
        print(rf.read())


def main():
    my_mp4_playlist(r"C:\Users\Eyal\PycharmProjects\campus-IL-self.py-course\songs", "Python Love Story")


if __name__ == "__main__":
    main()
