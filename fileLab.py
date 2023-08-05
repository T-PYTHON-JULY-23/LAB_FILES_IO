import os

print("Welcome to TO-DO list program..")
print("*remind: you can enter \"exit\" to close the program")
user_choice=input("Do you want to add a new To-Do item? y or n  ")
while user_choice!="exit":
    file=open('to_do.txt', "a+", encoding="utf-8")

    if user_choice.lower() =="y":  
        to_do=input("enter your to-do: ")
        file.write("\n"+to_do)
    elif user_choice.lower()=="n":
        user=input(" do you want to list your To-Do items ? y or n ")
        if user.lower() =="y":
            file.seek(0)
            content = file.read()
            print("TO-DO list :\n", content)   
    user_choice=input("do you want to add new item? y or n ")
else:
     print("thank you for using the To-Do program, come back again soon..")
file.close()

