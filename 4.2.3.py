the_temp = input("Insert the temperature you would like to convert: ")
the_temp_number = float(the_temp[:-1])
the_answer = -1, 'E'
if the_temp[-1].lower() == 'c':
    the_answer = (9 * the_temp_number + 160) / 5, 'F'
elif the_temp[-1].lower() == 'f':
    the_answer = (5 * the_temp_number - 160) / 9, 'C'

print(str(the_answer[0]) + the_answer[1])