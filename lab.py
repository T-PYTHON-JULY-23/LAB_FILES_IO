
def To_Do_List():
    exit = True
    user_input = ''
    listInput = ''

    while exit :
        print("-"*20)
        user_input = input("Do you want to add a new To-Do item? answer by \"y\" for yes and \"n\" for no:\n")
        if user_input.lower() == 'y':
            print("-"*20)
            ToDoInput= input("Type in new To-Do item:\n")
            file = open("to_do.txt", "a", encoding="utf-8")
            file.write(f"{ToDoInput}\n")
            file.close()
        elif user_input.lower() == 'n':
            print("-"*20)
            listInput= input("do you want to list your To-Do items ? answer \"y\" for yes and \"n\" for no:\n")
            if listInput.lower() == 'y':
                file = open("to_do.txt", "r", encoding="utf-8")
                content = file.read()
                file.close()
                print("-"*20)
                print("To-Do List :\n", content)
                
                
        if user_input.lower() == 'exit' or listInput.lower()  == 'exit':
            exit = False
            print("-"*20)
            print("Thank you for using the To-Do program, come back again soon")




To_Do_List()