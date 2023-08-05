import os

print("Welcome to TO-DO list program..")
userChoice=input("Do you want to add a new To-Do item? y or n or exit  ")
while userChoice!="exit":
    file=open('to_do.txt', "a+", encoding="utf-8")
    #file is variable 

    if userChoice =="y":  
        toDo=input("enter your to-do: ")
        file.write("\n"+toDo)


    elif userChoice=="n":
        anotherOption=input(" do you want to list your To-Do items ? y or n or exit ")
        if anotherOption =="y":
            file.seek(0)
            allList = file.read()
            print("TO-DO list :\n", allList)
    userChoice=input("do you want to add new item? y or n or exit ")
    file.close()    
else:
    print("thank you for using the To-Do program, come back again soon..")


