print("----- Wlecom in  To-Do List -----")

while True:
    item = input("\nyou want to add a new To-Do item? answer by yes or no  or exit: \n")

    if item.lower() in 'yes':
        user = input("\nEnter To-Do item:\n")
        file_item = open("to_do.txt", 'a+', encoding='utf-8')
        file_item.write('\n'+ user)
        file_item.close
        
    
    elif item.lower() in 'no':
        user_no =input("\ndo you want to list your To-Do items? \n")
        if user_no == 'yes':
            file_item = open("to_do.txt", 'r', encoding='utf-8')
            to_do_read = file_item.readlines()
            file_item.close
            print("list of the To-Do items: ", to_do_read )

    elif item.lower() in 'exit':
            print("\nthank you for using the To-Do program, come back again soon")
            break
    else:
          print("\nPlease enter yes or no or exit ")


