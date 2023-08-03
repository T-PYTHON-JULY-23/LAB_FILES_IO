userAns=''
count = 1
while userAns !='exit':
    userAns=input('do you want to add a new To-Do item? answer by "y" for yes and "n" for no:')
    if userAns == 'y':
        newLine = input('type here: ')
        file = open('To_Do_List.txt', "a", encoding="utf-8")
        file.write(f'{str(count)}. {newLine}\n')
        count =count+1
        file.close()
    elif userAns == 'n':
        userAns = input('do you want to list your To-Do items ? answer "y" for yes and "n" for no: ')
        if userAns == 'y':
            file = open("To_Do_List.txt", "r", encoding="utf-8")
            content = file.read()
            print('-----To Do List-----\n', content)
            file.close()
        else:
            print('type "exit" to exit')
print('thank you for using the To-Do program, come back again soon')