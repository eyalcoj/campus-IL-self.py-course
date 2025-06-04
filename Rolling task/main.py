import random

HANGMAN_ASCII_ART = r"""
Welcome to the game Hangman

     _    _
    | |  | |
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
    |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/"""

MAX_TRIES = 6

FILE_PATH = r"C:\Users\Eyal\PycharmProjects\campus-IL-self.py-course\Rolling task\word.txt"

STATE0 = r"""
        x-------x
        
        
        
        
        
        """

STATE1 = r"""
        x-------x
        |
        |
        |
        |
        |     
        """

STATE2 = r"""
        x-------x
        |       |
        |       0
        |
        |
        |   
        """

STATE3 = r"""
        x-------x
        |       |
        |       0
        |       |
        |
        |
        """

STATE4 = r"""
        x-------x
        |       |
        |       0
        |      /|\
        |
        |
        """

STATE5 = r"""
        x-------x
        |       |
        |       0
        |      /|\
        |      /
        |
        """

STATE6 = r"""
        x-------x
        |       |
        |       0
        |      /|\
        |      / \
        |
        """

HANGMAN_PHOTOS = dict()
HANGMAN_PHOTOS[0] = STATE0
HANGMAN_PHOTOS[1] = STATE1
HANGMAN_PHOTOS[2] = STATE2
HANGMAN_PHOTOS[3] = STATE3
HANGMAN_PHOTOS[4] = STATE4
HANGMAN_PHOTOS[5] = STATE5
HANGMAN_PHOTOS[6] = STATE6


def show_hidden_word(secret_word, old_letters_guessed):
    """
    this method sh show the progress of guessed word
    :param secret_word: the secret word itself
    :param old_letters_guessed: all the guessed words
    :type secret_word: str
    :type old_letters_guessed: list
    :return: nothing
    :rtype: None
    """

    all_the_guess = list()

    for char in secret_word:
        if char in old_letters_guessed:
            all_the_guess.append(char)
        else:
            all_the_guess.append('_')

    print(' '.join(all_the_guess))


def check_win(secret_word, old_letters_guessed):
    """
    check if the player guessed all the letters from the secret word
    :param secret_word: the secret word itself
    :param old_letters_guessed: all the guessed words
    :type secret_word: str
    :type old_letters_guessed: list
    :return: if the player has wan
    :rtype: bool
    """
    the_secret_word_list = list(secret_word)

    for letter in old_letters_guessed:
        count_letters = the_secret_word_list.count(letter)
        for i in range(0, count_letters):
            the_secret_word_list.remove(letter)

    return len(the_secret_word_list) == 0


def is_valid_input(letter_guessed: str, old_letters_guessed: list):
    """ the method check if the str is valid
    :param letter_guessed: the new input value
    :param old_letters_guessed: the old input value
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: is valid or not
    :rtype: bool
    """
    if len(letter_guessed) > 1 and not letter_guessed.isalpha():
        print("E3")
        return False
    elif not letter_guessed.isalpha():
        print("E2")
        return False
    elif len(letter_guessed) > 1:
        print("E1")
        return False
    elif letter_guessed in old_letters_guessed:
        print("E4")
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    the program print all the letters that has all redy been used wth an -> between them if it has been used. and return the if it in the old letters guess
    :param letter_guessed: the letter it tried to insert
    :param old_letters_guessed: all the old letters
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: if it in the old letters guess
    :rtype: bool
    """

    is_correct_input = is_valid_input(letter_guessed, old_letters_guessed)
    if is_correct_input:
        old_letters_guessed.append(letter_guessed)
    else:
        old_letters_guessed.sort()
        new_str_list = "->".join(old_letters_guessed)
        print("X")
        print(new_str_list)
    return is_correct_input


def print_hangman(num_of_tries):
    """
    the function prints one of the seven states of the hanging man
    :param num_of_tries: which represents the number of failed attempts by the user so far
    :type num_of_tries: int
    :return: nothing
    :rtype: None
    """
    print(HANGMAN_PHOTOS[num_of_tries])


def choose_word(file_path, index):
    """
    Choose a word for the player to be the secret word to guess, from a text file containing a list of words separated by spaces.
    :param file_path: Path to the text file
    :param index: Location of a specific word in a file
    :type file_path: str
    :type index: int
    :return: A tuple consisting of two elements. The number of distinct words in the file and the word at the position
    received as an argument to the function.
    :rtype: tuple
    """

    with open(file_path) as rf:
        all_the_words = rf.read().replace("\n", " ").split(" ")
        amount_of_words = len(all_the_words)

        all_of_unic_words = list()
        for word in all_the_words:
            if word not in all_of_unic_words:
                all_of_unic_words.append(word)

        amount_of_unic_words = len(all_of_unic_words)
        return amount_of_unic_words, all_the_words[(index - 1) % amount_of_words]


def main():
    num_of_tries = 0
    old_letters_guessed = list()

    # 1.
    print(HANGMAN_ASCII_ART)
    print(f"Number of tries:{MAX_TRIES} ")

    # 2.
    file_path_for_choosing_word = input("Please enter a the file path: ")
    random_number_for_choosing_word = int(input("Please enter a random number: "))
    secret_word = choose_word(file_path_for_choosing_word, random_number_for_choosing_word)[1]

    # 3.
    print_hangman(num_of_tries)

    # 4.
    show_hidden_word(secret_word, old_letters_guessed)

    # 5.
    while not check_win(secret_word, old_letters_guessed) and num_of_tries < MAX_TRIES:
        letter_guess = input("Guess a letter: ").lower()
        is_update_letter_guessed = try_update_letter_guessed(letter_guess, old_letters_guessed)
        if is_update_letter_guessed:
            if letter_guess not in secret_word:
                num_of_tries += 1

            # 6.
            if not check_win(secret_word, old_letters_guessed):
                print_hangman(num_of_tries)
            show_hidden_word(secret_word, old_letters_guessed)

    # 7.
    if check_win(secret_word, old_letters_guessed):
        print("WIN")
    else:
        print("LOST")


if __name__ == '__main__':
    main()
