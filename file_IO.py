print("📋 Welcome to the To-Do program 📋")
while True:
    answer1= input("do you want to add a new To-Do item? answer by 'y' for yes and 'n' for no and 'exit' for exit from the program 😊 ")
    if answer1 == 'y': # if the user answer yes <<
        to_Do_item = input("please type in the new To-Do item :") 
        file = open("to_do.txt" , "w" ,encoding="utf-8")# he will type his to-do list andthen save it inside the file
        file.writelines(to_Do_item)
        file.close()
    elif answer1 == 'n': # if the user answer no <<
        answer2 = input("do you want to list your To-Do items ?") # the program will ask him if he want to print the list or no 
        if answer2 == 'y':
            file = open("to_do.txt" , "r" ,encoding= "utf-8")
            content = file.read()
            file.close()
            print(content)
        elif answer2 == 'n' : # if he answer no the program will ignore this Question and eturn again to ther first question and ask again 
            continue
    elif answer1 == 'exit' : # if the user wtite 'exit' , the program will print a thank message and exit from the program 
        print("  thank you for using the To-Do program, come back again soon ...🥰👋")
        break


