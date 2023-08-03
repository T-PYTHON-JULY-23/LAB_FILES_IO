exit = ''
while exit != 'e':
    usr_input=input("do you want to add a new To-Do item? answer by 'y' for yes and 'n' for no and 'e' for exit: ")
    if usr_input == 'y':
        file = open ("to_do.txt","w",encoding="utf-8")
        file.write(input("what to add more? "))
        file.close()
    elif usr_input == 'n':
        usr2_input = input('do you want to list your To-Do items ? answer "y" for yes and "n" for no "e" to exit: ')
        if usr2_input == 'y':
           file = open('to_do.txt', "r", encoding="utf-8")
           content = file.read()
           print("content of the file: ",content)
           file.close()
        elif usr2_input=="n":
             continue
        elif usr2_input == "e":
             break
    elif usr_input == "e":
            break




