

#file = open("to_do.txt","x",encoding="utf-8")
def To_Do_List ():

 
 while True:
    user=input("do you want to add a new To-Do item? press y for yes and n for no: ")
    if user.lower() == "y":
      ask1=input("what type in new To-Do item?")
      file = open("to_do.txt","a+")
      file.seek(2)
      file.write( '\n' + ask1)
      file.close()

    elif user.lower() == "n":
      ask2=input("do you want to list your To-Do items ?")
      if ask2.lower() == "y":
        file = open("to_do.txt","r")
        content=file.read()
        file.close()
        print(content ) 

      else:
         print("press EXIT if you want exit the program ")

    elif user.upper()=='EXIT':
      print("Thank you for using the To-Do program, come back again soony")
      break
    


To_Do_List()