import json

def add_task():
    title=input("Enter tilte of the task: ".title())
    date=input("Enter date of the task: ".title())
    done=False

    x={}
    x[title]={
        'date':date,
        'done':done,
    }
    try:
        with open('output.json', 'r') as file:
            try:
                full_data = json.load(file)
            except:
                full_data={}
        

            full_data[title]={
                'date':date,
                'done':done,}
    except:
        with open('output.json', 'w') as file:
          json.dump(x, file, indent=4)            
          return None
        
    with open('output.json', 'w') as file:
        json.dump(full_data, file, indent=4)

def print_tasks():
    full=None
    count=0
    try :
        with open('output.json','r')as f :
            full=json.load(f)
            for key,value in full.items():
                print(f"{count+1}- {key} - {value['date']} - {'DONE' if value['done'] else 'NOT DONE'} ")
                count+=1
    except:
        print("add task first ")
def done_task():
    title=input("Enter task to complate: ".title()).lower()
    full=None
    try:
        with open('output.json','r')as f :
            full=json.load(f)
    except:
        print("No data found ")
    if title in full.keys():
        full[title].update(done=True)
    else :
        print('Taske doesnt exit ')
    with open('output.json', 'w') as file:
        json.dump(full, file, indent=4)
print("1 to add task \n2 to see all tasks\n3 to complate taske or exit to leave".title())
user_input=input("Enter what you would like to do: ".title()).lower()

while user_input!='exit':
    if user_input=='1':
        add_task()
    elif user_input=='2':
        print_tasks()
    elif user_input=='3':
        done_task()
    else :
        print("Wrone value ")
    user_input=input("Enter what you would like to do".title()).lower()
