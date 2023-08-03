'''
Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
If the user answers yes , then ask the user to type in his new To-Do item . Then save that To-Do item inside the a file to_do.txt on a new line.
If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no.
If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
Then return again to ther first question and ask again, you coninue this untill the user types in "exit" , then you exit the program. and print to the user "thank you for using the To-Do program, come back again soon"
'''
def text_do_it():
    ask_user = input('do you want to add a new To-Do item? answer by "y" for yes and "n" for no. : ')
    if ask_user == 'y':
        input_user_y =input("Please Enter what to want do it ?")
        file = open("to_do.txt", "a+", encoding="utf-8")
        file.write(f"{input_user_y}\n\n")
        file.close()
        text_do_it()
    elif ask_user == 'n':
        ask_user_for_list_item =input('do you want to list your To-Do items ? answer "y" for yes and "n" for no. : ')
        if ask_user_for_list_item == 'y':
            file = file = open("to_do.txt", "r", encoding="utf-8")
            content = file.read()
            print(content)
            print()
            text_do_it()
        elif ask_user_for_list_item == 'n':
            write_again = input("Do want to write again ? answer y for yes and exit for exit from program : ")
            if write_again == 'y':
                text_do_it()
            elif write_again == "exit":
                print("-----------------------------------------------------------")
                print("thank you for using the To-Do program, come back again soon")
                print("-----------------------------------------------------------")
                return 0
    else:
        print("Please write y or n !")
        text_do_it()
text_do_it()