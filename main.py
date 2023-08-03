import os
while True:
    to_do = input("do you want to add a new To-Do item  press Y / N \n to exti enter exit : ")
    print("-"*20)
    if to_do.upper() =='Y':
        user= input("type what you want in your new To-Do item: ")
        file = open('test.txt', "a+", encoding="utf-8")
        file.write(user+"\n")
        file.close()

    elif to_do.upper() =='N':
        while True:
            user_list= input(" do you want to show list your To-Do items ? Y \ N : ")
            if user_list.upper()=='Y':
             
             file = open("test.txt", "r", encoding="utf-8")
             content = file.read()
             file.close()
             print("content of file :", content)

            elif user_list.upper()=='N':
             print('to exit enter exit and thank you')
             
             break
        
    elif to_do.lower() =='exit':
        print('_'*20)
        print("thank you for using the To-Do program, come back again soon")
        print('_'*20)
        break
    else:
        print("please select Y or N olny -_- ")