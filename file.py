
while True:
  file = open("to_do.txt", "a+", encoding="utf-8")
  your_items = input("do you want to add a new To-Do item? by 'y' for 'yes' and 'n' for 'no'")

  if your_items == 'y':
   x=input("new To-Do item ")
   file.write(x+"\n")
   file.close()
     
  elif your_items =='n' :
    z = input( "do you want to list your To-Do items ?")
    
    if your_items == 'y':
      file.seek(0)
      print(file.read(z))


  elif your_items == 'exit':
    print ( "thank you for using the To-Do program, come back again soon")
    break
  