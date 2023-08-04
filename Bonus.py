import json


def json_module():
    
    print("-"*20)
    user_input = input("Do you want to add a new To-Do item? answer by \"y\" for yes and \"n\" for no:\n")
    if user_input.lower() == 'y':
        title = input("Enter the title of the task:\n")
        date_time = input("Enter the date and time of the task:\n")
        
        To_Do_item = {"title" : title,
        "date_time" : date_time,
        "done" : False }
        json_object = json.dumps(To_Do_item, indent=3)
        with open("ToDowithj.json", "w") as outfile: outfile.write(json_object)
    if user_input.lower() =='n':
        listInput= input("do you want to display your To-Do items ? answer \"y\" for yes and \"n\" for no:\n")
        if listInput.lower() == 'y':
            with open('ToDowithj.json', 'r') as openfile: j_object = json.load(openfile)
            print(j_object)
        if listInput.lower() =='n':
            with open('ToDowithj.json', 'r') as openfile: data = json.load(openfile)
            searchInput= input("do you want to search your tasks using the title? answer \"y\" for yes and \"n\" for no:\n")
            if searchInput.lower() == 'y':
                taskinput= input("Enter taske title:\n ")
                if taskinput in data:
                    #if data['done'] == True:
                    print(f"{data['title']} - {data['date_time']} - DONE\n")
                    #elif data['done'] == False:   
                       # print(f"{data['title']} - {data['date_time']} - NOT DONE\n") 
                else:
                    print("Not fond\n")

            if searchInput.lower() == 'n':
                donnetaskInput= input("do you want to mark a specific Task as Done.? answer \"y\" for yes and \"n\" for no:\n")
                
                with open('ToDowithj.json', 'r+', encoding='utf-8') as openfile: filedata = json.load(openfile)
                if donnetaskInput.lower() == 'y':
                    changeinput= input("Enter taske title:\n")
                    if taskinput in filedata:
                        filedata[1]['done'] = True
                        print("Done changing Task to Done\n")
                    else:
                        print("Taske title not found:\n")



json_module()
              
              


