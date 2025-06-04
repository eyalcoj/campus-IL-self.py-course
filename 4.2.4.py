import calendar

the_date = input("Enter a date: ").replace(" ", "")

day_number = calendar.weekday(int(the_date[-4:]), int(the_date[-7:-5]), int(the_date[-10:-8]))
print(day_number)
if day_number == 0:
    print("monday")
elif day_number == 1:
    print("tuesday")
elif day_number == 2:
    print("wednesday")
elif day_number == 3:
    print("thursday")
elif day_number == 4:
    print("friday")
elif day_number == 5:
    print("saturday")
elif day_number == 6:
    print("sunday")

else:
    print("what the hell")

