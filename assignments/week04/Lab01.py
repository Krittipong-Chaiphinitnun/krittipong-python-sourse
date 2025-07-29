"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("Krittipong",19, "Sriracha", "Thailand")  # name, age, city, country
    hobbies = []

    while True:
        print("\nPersonal Information Manager")
        print("1. Display all information")
        print("2. Add new hobbies")
        print("3. Remove hobbies")
        print("4. Update age")
        print("5. Exit")
        choice = input("Enter your choice: ")
    
        # Your code here
        if choice == "1":
            # display info
            print("Name:",person[0])
            print("Age:",person[1])
            print("City:",person[2])
            print("Country:",person[3])
            print("Hobbies:",hobbies)
            

        # add hobby
        elif choice == "2":
            new_hobby = input("Enter new hobby: ")
            hobbies.append(new_hobby)
            print("Hobby added.")
        # remove hobbies
        elif choice == "3":
            rem_hobby = input("Enter hobby to remove: ")
            if rem_hobby in hobbies:
                hobbies.remove(rem_hobby)
                print("Hobby removed.")
            else:
                print("Hobby not found.")

        # update age
        elif choice == "4":
            new_age = input("Enter new age: ")
            if new_age.isdigit():
                person = (person[0], int(new_age), person[2], person[3])
                print("Age updated.")
            else:
                print("Invalid age.")

        # exit
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")                

    if __name__ == "__main__":
        personal_info_manager()