print ("Hello to our program! To-Do! ")

while True: #!= exit:
    Question_1 = input(("Do you want to add a new To-Do item? answer 'y' for yes and'n' For no,and exit if you Don't want to continue:"))
    if Question_1 == 'y':
        file = open ("To_Do.txt" , "a+" , encoding ="utf-8")
        conuevt = input ("add what do you want :")
        file.write('\n'+conuevt)
        file.close()
    
    elif Question_1 == 'n':
        Question_2 = input(("Do you want to list your To-Do items? answer'y' for yes and'n' For no,and 'exit' if you Don't want to continue:"))
        if Question_2 == 'y':
           file = open("To_Do.txt", "r", encoding="utf-8")
           content = file.readlines()
           print("content of the file: ",content)
           file.close()
    #elif ask_useer == 'n':
       #continue
    elif Question_1 == "exit":
        print("thank you for using our Program the To-Do!, come back again soon!")
        break
    #elif Question_1 == exit :
        #print("thank you for using the To-Do program, come back again soon!")
        #break
    else:
        print("You're did not choose 'y' or 'n' or 'exit!")

 
 