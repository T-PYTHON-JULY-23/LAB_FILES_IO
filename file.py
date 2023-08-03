
q=True
while q:
 
 add_item=input(" do you want to add a new To-Do item? answer by \"y\" for yes and \"n\" for no if you exit type exit ")
 file=open("to_do.txt","+a",encoding="utf-8")


 if add_item=="y":
    add_infile=input("type a new To-Do item ")
    content=file.write(add_infile+"\n")
    file.close()



 elif add_item=="n":
  print_list=input("do you want to list your To-Do items ? answer \"y\" for yes and \"n\" for no:   ")
  if print_list=="y":
    file.seek(0)
    listi=file.read()
    print (listi)
   
    file.close() 
    
 elif add_item=="exit":
     q=False
     print("thank you for using the To-Do program, come back again soon")
 