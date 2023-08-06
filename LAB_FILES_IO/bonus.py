
'''

import json

to_do= {}


def add_task():
    title = input("Please enter the title: ")
    date = input("please enter the date as d-m-y: ")
    done = False

    d =  {}
    to_do[title] ={
        "date": date,
        "done": False
    }
    
    with open("file.json", "w") as file:
         json.dump(to_do, file)

add_task()

from datetime import datetime
now = datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)

'''
import json
from datetime import datetime
'''

print("select what you wnat to do: ")
print("1- To add new TO-Do-Itme \n2- To list the TO-Do-Itme" )

'''
to_do ={}

def add_list():
    to_do['title']=input("Enter title of the task: ")
    to_do['date']=input("Enter date of the task:  ")
    to_do['done']=False


    with open('to_do.json','a+') as file:
        json.dump(to_do,file,indent=4)
    return(to_do)



def list_task():
    with open('to_do.json', 'r+') as f:
        json_content = json.load(f)
        for key , value in json_content.items():
            print(key, value)


list_task()



'''

        for key , value in to_do.items:
            print(f"{key}-{value['date']}- {'DONE' if value['done'] else 'NOT DONE'}")

'''





        

                    



                
                





'''
while True:
    quit=input("Enter Y/N to continue")
    if quit.lower()=='n':
        break
    else:
       out['to_do_itme']= add_list()



'''

'''
while True:
    out={}

    quit=input("Enter 1 to add new task")
    if quit.lower()=='n':
        break
    else:
       out['to_do_itme']= add_list()
       with open('to_do.json','w') as file:
          json.dump(out,file,indent=2)

'''

