import math

the_word = input("Enter a word: ").lower().replace(" ", "")
the_word_len = len(the_word)
the_first_half = the_word[:math.floor(the_word_len/2)]
the_second_half = the_word[-1:math.ceil(the_word_len/2) - 1: -1]

if the_first_half != the_second_half:
    print("NOT")
else:
    print("OK")
