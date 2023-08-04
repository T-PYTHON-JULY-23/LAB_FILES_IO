# Ask the user if they want to add a new To-Do item
while True:
    choice = input("Do you want to add a new To-Do item? (y/n/exit) ")
    if choice.lower() == "y":
        # Get the new To-Do item from the user
        new_item = input("Enter your new To-Do item: ")
        # Save the new To-Do item to the file
        with open("to_do.txt", "a") as f:
            f.write(new_item + "\n")
    elif choice.lower() == "n":
        # Ask the user if they want to list their To-Do items
        while True:
            list_choice = input("Do you want to list your To-Do items? (y/n) ")
            if list_choice.lower() == "y":
                # Read the To-Do items from the file and print them
                with open("to_do.txt", "r") as f:
                    print("Your To-Do List:")
                    for line in f:
                        print(line.strip())
            elif list_choice.lower() == "n":
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
    elif choice.lower() == "exit":
        break
    else:
        print("Invalid input. Please enter 'y', 'n', or 'exit'.")

print("Thank you for using the To-Do program, come back again soon!")

#---------------------------------------------------------
