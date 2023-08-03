
while True:
 answer = input("Do you want to add a new To-Do item? answer by 'y' for yes and 'n' for no or exit: ")

 if answer == 'y':
  toDo_item = input("type in your new To-Do item: ")
  file = open("to_do.txt", "a+", encoding="utf-8")
  file.write(toDo_item+"\n")
  file.close()

 elif answer == 'n':
   view_toDo = input("do you want to list your To-Do items ? answer 'y' for yes and 'n'")
   if view_toDo == 'y':
    file = open("to_do.txt", "r", encoding="utf-8")
    content = file.read()
    file.close()
    print (content)
    continue

   elif view_toDo == 'n':
    continue
   else:
    raise TypeError ("Invalid. Please use 'y' for yes or 'n' for no.")

 elif answer == 'exit':
  print("Thank you for using the To-Do program, come back again soon")
  exit()
 else:
  raise TypeError ("Invalid. Please use 'y' for yes or 'n' for no.")


