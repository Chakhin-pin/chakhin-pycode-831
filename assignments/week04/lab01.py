person = ("Chakhin", 19, "Chonburi", "Thailand")  # name, age, city, country
hobbies = ["exercise", "sleeping"]

while True:
        
    print("\n---Personal Information Manager ---")
    print("1.Display all information")
    print("2.Add new hobby")
    print("3.Remove hobby")
    print("4.Update age")

    choice= input ("Enter your choice")

    # Your code here
    if choice == "1":
        print("Name: ",person[0])
        print("Age: ",person[1])
        print("City: ",person[2])
        print("Country: ",person[3])
        print("Hobbies: ",hobbies)

    #add hobby
    elif choice == "2":
        hobby = input("What is your hobby?")
        hobbies.append(hobby)
        print("hobby added complete!")

    #remove hobby
    elif choice == "3":
        remove_hobby = input("Enter hobby to remove: ")
        if remove_hobby in hobbies:
            hobbies.remove(remove_hobby)
            print("hobby removed coplete!")
        else:
            print("hobby not found!")

    #new age 
    elif choice == "4":
        new_age = int(input("Enter new age:"))
        person = (person[0], new_age, person[2], person[3])
        print("age updated complete!")

else:
    print("Invalid choice, please try again.")