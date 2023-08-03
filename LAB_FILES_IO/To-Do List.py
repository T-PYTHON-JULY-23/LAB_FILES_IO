
print("---wlcome you in To-Do List program--- ")

while  True:

    quistion_anwser = input('do you want to add a new To-Do item? \nanswer by "y" for yes and "n" for no or exit to leave the program: ')

    if quistion_anwser.lower() == "y":
        user_input1= input("please enter a new To-Do item: ")
        file = open("to_do.txt", "a+", encoding="utf-8")
        file.writelines(user_input1 + "\n")
        file.close()


    elif quistion_anwser.lower() == "n":
        print("do you want to list your To-Do items ? ")
        user_input2=input ('answer by "y" for yes and "n" for no:')
        if user_input2.lower() == "y":
            file = open("to_do.txt", "r", encoding="utf-8")
            file.seek(0)
            content = file.read()
            print("the To-Do items are: " , content)
            file.close()
            print("-"*30)
            
            

    elif  quistion_anwser.lower() == "exit":
        print("thank you for using the To-Do program, come back again soon")
        break

    else:
        print('Please answer by "y" for yes and "n" for no or exit to leave the p rogram :')
        
        





