from datetime import date


def main():
    ID = dict()
    ID["first_name"] = "Mariah"
    ID["last_name"] = "Carey"
    ID["birth_date"] = "27.03.1970"
    ID["hobbies"] = ["Sing", "Compose", "Act"]

    actoin_number = int(input("Please enter a number to diced the action: "))

    if actoin_number == 1:
        print(ID["first_name"])
    elif actoin_number == 2:
        print(ID["birth_date"][3:5])
    elif actoin_number == 3:
        print(ID["hobbies"])
    elif actoin_number == 4:
        print(ID["hobbies"][-1])
    elif actoin_number == 5:
        ID["hobbies"].append("Cooking")
        print(ID["hobbies"])
    elif actoin_number == 6:
        ID["birth_date"] = (int(ID["birth_date"][-4:]), int(ID["birth_date"][-7:-5]), int(ID["birth_date"][-10:-8]))
        print(ID["birth_date"])
    elif actoin_number == 7:
        ID["birth_date"] = (int(ID["birth_date"][-4:]), int(ID["birth_date"][-7:-5]), int(ID["birth_date"][-10:-8]))
        today = date.today()
        ID["age"] = today.year - ID["birth_date"][0] - ((today.month, today.day) < (ID["birth_date"][1], ID["birth_date"][2]))
        print(ID["age"])
    else:
        print("check you input")


if __name__ == "__main__":
    main()
