import os

while True:
    choice1 = input(" do you want to add a new To-Do item? answer by \"y\" for yes and \"n\" for no and \"exit\" to exit the program : ")
    
    if choice1 == "exit":
        print("Thanks for using the 'TO-DO program'")
        break

    elif choice1.lower() == 'y':
        task = input("please enter the task you want to add : ")
        file = open("to-do-list.txt", 'a', encoding="utf-8")
        file.write(f"{task}\n")
        file.close()

    elif choice1.lower() == 'n':
        choice2 = input("do you want to list your To-Do items ? answer \"y\" for yes and \"n\" for no : ")
        
        if choice2.lower() == 'y':
            file = open("to-do-list.txt", "r", encoding="utf-8")
            task_list = file.readlines()
            file.close()
            for task in task_list:
                print(task[:-1])
        
        elif choice2.lower() == 'n':
            continue
        
        else:
            print(f"'{choice2}' is not from the choices i give to you")
    
    else:
        print(f"'{choice1}' is not from the choices i give to you")