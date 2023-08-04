import os



while True:
    user_input = input("Do you want to add a new To-Do item? (y/n) ")

    if user_input.lower() == "y":
        to_do_item = input("Enter your new To-Do item: ")
        
        filename= open("To-Do.txt", "a+", encoding ="utf-8")
        filename.write(to_do_item + "\n")
        print("To-Do item added!")
    elif user_input.lower() == "n":
        user_input = input("Do you want to list your To-Do items? (y/n) ")
        if user_input.lower() == "y":
         filename= open("To-Do.txt", "r", encoding ="utf-8")
        to_do_list = filename.readlines()
        print("Your To-Do list:")
        for item in to_do_list:
                    print("- " + item.strip())
    elif user_input.lower() == "n":
            break

    print("thank you for using the To-Do program, come back again soon ")
        
    
    

