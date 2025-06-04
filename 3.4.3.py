the_input = input("Please enter a string: ")
the_input_length = len(the_input)
the_answer = the_input[:the_input_length//2].lower() + the_input[the_input_length//2:].upper()

print(the_answer)