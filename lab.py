# Using what you learned about Python File I/O , we want to make a progeram called To-Do List , this program should do the following:

#     Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
#     If the user answers yes , then ask the user to type in his new To-Do item . Then save that To-Do item inside the a file to_do.txt on a new line.
#     If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no.
#     If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
#     Then return again to ther first question and ask again, you coninue this untill the user types in "exit" , then you exit the program. and print to the user "thank you for using the To-Do program, come back again soon"





import os

while True:
    print("Do you want to add a new To-Do item? (y/n/exit)")
    choice = input().lower()
    if choice == 'y':
        todo = input("Enter To-Do item: ")
        with open("to_do.txt", "a") as f:
            f.write(todo + "\n")
    elif choice == 'n':
        print("Do you want to list your To-Do items? (y/n/exit)")
        choice = input().lower()
        if choice == 'y':
            os.system('cls' if os.name == 'nt' else 'clear') # clear the screen
            with open("to_do.txt") as f:
                data = f.read().split("\n")
                for line in data:
                    print(line)
        elif choice == 'exit':
            break
    elif choice == 'exit':
        break
    else:
        print("Invalid input. Please enter 'y', 'n', or 'exit'.")
print("Thank you for using the To-Do program, come back again soon!")
f.close()