def is_anagrams(word1, word2):
    """
    check if anagrams
    :param word1: the frst word
    :param word2: the second word
    :type word1: str
    :type word2: str
    :return: is the words anagrams
    :rtype: bool
    """

    return sorted(word1) == sorted(word2)


def sort_anagrams(list_of_strings):
    """
    make a list of all the anagrams
    :param list_of_strings: list of string, every string is only one word (without space)
    :type list_of_strings: list
    :return: all the anagrams word sorted
    :rtype: list of list
    """
    anagrams_list = list()
    outer_remove = 0
    i = 0
    while i - outer_remove < len(list_of_strings):
        anagram_list = list([list_of_strings[i - outer_remove]])
        inner_remove = 0
        j = i - outer_remove + 1
        while j - inner_remove < len(list_of_strings):
            if is_anagrams(list_of_strings[i - outer_remove],
                           list_of_strings[j - inner_remove]):
                anagram_list.append(list_of_strings[j - inner_remove])
                list_of_strings.remove(list_of_strings[j - inner_remove])
                inner_remove += 1
            j += 1

        anagrams_list.append(anagram_list)
        list_of_strings.remove(list_of_strings[i - outer_remove])
        outer_remove += 1
        i += 1

    return anagrams_list


def main():
    list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
    print(sort_anagrams(list_of_words))


if __name__ == "__main__":
    main()
