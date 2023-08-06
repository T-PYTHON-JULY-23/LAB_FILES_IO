import datetime
import json 
q=True

while q:
 
 add_item=input(" do you want to add a new To-Do item? answer by \"y\" for yes and \"n\" for no if you exit type exit ")
 
 if add_item=="y":
   
  title=input("type a new To-Do item ")
  time=str(datetime.datetime.now())
  is_done=False
  to_do  ={"title":title,"time":time,"is done":is_done}
  
  y = json.dumps(to_do)
  
  cont=+1
  
 elif add_item=="n":

  print_list=input("do you want to list your To-Do items ? answer \"y\" for yes and \"n\" for no:   ")
  if print_list=="y":
   serch=json.loads(y)
   if serch["is done"]==True:
    d="DONE"
   else:
      d="NOT DONE"
   print(f"{cont}: {serch['title']} - {serch['time']} - {d}")
    
 elif add_item=="exit":
     q=False
     print("thank you for using the To-Do program, come back again soon")
 