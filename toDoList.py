


def modifyToDoList():

    while True :
        toDoList = str(input("do you want to add a new To-Do item? answer by y for yes and n for no: "))
        if toDoList.lower() == "y" :
            newToDoList = input("pleas type in your new To-Do item:")
            file = open("ToDoList.txt" , "a+" , encoding="utf-8")
            file.write(newToDoList+ "\n")
            file.close()
        elif toDoList.lower() == "n" :
            listToDo = input("do you want to list your To-Do items ? answer y for yes and n for no (if you want to exit write 'exit'): ")
            if listToDo.lower() == "y":
                file = open("ToDoList.txt" , "r+" , encoding="utf-8")
                contsnt=file.read()
                file.close()
                print(contsnt)

            elif listToDo.lower() == "n" or "exit":
                print("Thank you for using the To-Do program, come back again soon!")
                break
        

        else:
            continue


modifyToDoList()