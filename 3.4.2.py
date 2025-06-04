the_msg = input("Please enter a string: ")
new_msg = the_msg[0] + the_msg[1:].replace(the_msg[0], "e")
print(new_msg)
