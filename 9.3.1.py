def my_mp3_playlist(file_path):
    """
    give a data on the songs
    :param file_path: the function accepts a file path as a parameter. The file represents a playlist of songs and has
     a fixed format consisting of the song name, the artist name (singer/band), and the length of the song, separated
      by a semicolon (;) without spaces.
    :type file_path: str
    :return: the data in a tuple
    :type: tuple
    """

    with open(file_path) as rf:
        lines = rf.readlines()
        for i_line in range(len(lines)):
            lines[i_line] = lines[i_line].split(";")

        max_song_length = int(lines[0][2].replace(":", ""))
        max_song_length_name = lines[0][0]

        # find the longest song
        for line in lines[1:]:
            song_length = int(line[2].replace(":", ""))
            song_length_name = line[0]
            if max_song_length < song_length:
                max_song_length = song_length
                song_length_name = max_song_length_name

        # find the most listen performer
        performers = dict()
        for line in lines:
            performer_name = line[1]
            if performer_name in performers:
                performers[performer_name] += 1
            else:
                performers[performer_name] = 1

        max_performer = list(performers.keys())[0]
        for performer in list(performers.keys())[1:]:
            if performers[max_performer] < performers[performer]:
                max_performer = performer

    return max_song_length_name, len(lines), max_performer


def main():
    print(my_mp3_playlist(r"C:\Users\Eyal\PycharmProjects\campus-IL-self.py-course\songs"))


if __name__ == "__main__":
    main()
