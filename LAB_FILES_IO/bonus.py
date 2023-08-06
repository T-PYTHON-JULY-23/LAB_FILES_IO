
import json
from datetime import datetime
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









        

                    



                
                






