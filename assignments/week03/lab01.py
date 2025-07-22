while True:
    try: 
        age = int (input("Enter age"))
        if age < 0:
            print("Age must more than 0.")
        elif age <= 12:
            print("You're Child")
        elif age <= 19:
            print("You're Teenager")
        elif age <= 59:
            print("You're Adult")
        else:
            print("You're senoir")
        break 
    except ValueError:
        print("Invalid age")




