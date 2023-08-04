import json
from time import gmtime, strftime





date = strftime("%Y-%m-%d %H:%M:%S", gmtime())


def text_do_it():
    ask_user = input('do you want to add a new To-Do item? answer by "y" for yes and "n" for no. : ')
    if ask_user == 'y':
        input_user_y =input("Please Enter what to want do it ?")
        task_done=input("Are you finish the list To-do items? answer by 'y' for yes and 'n' for no. :")
        if task_done=='y':
            done="Done"
            # ------ Using json -------
            json_dict = {"title":input_user_y,"date":date,"done":done}
            with open("new_json.json", "w", encoding="utf-8") as f:
                json.dump(json_dict, f, indent=4)
            print()
            text_do_it()
        elif task_done=="n":
            done="Not Done"
            # ------ Using json -------
            json_dict = {"title":input_user_y,"date":date,"done":done}
            with open("new_json.json", "w", encoding="utf-8") as f:
                json.dump(json_dict, f, indent=4)
            print()
            text_do_it()



    elif ask_user == 'n':
        ask_user_for_list_item =input('do you want to list your To-Do items? answer "y" for yes and "n" for no. : ')
        if ask_user_for_list_item == 'y':
            title_input = input("Enter the the title of the To-do item :")
            with open("new_json.json", "r", encoding="utf-8") as f:
                show_json=json.load(f)
            if title_input == show_json["title"]:
                print(f"{show_json['title']} - {show_json['date']} - {show_json['done']}")
            else:
                print("There is no title like this")


        elif ask_user_for_list_item == 'n':
            write_again = input("Do you want to write again ? answer y for yes and exit for exit from program : ")
            if write_again == 'y':
                text_do_it()
                print()
            elif write_again == "exit":
                print("-----------------------------------------------------------")
                print("thank you for using the To-Do program, come back again soon")
                print("-----------------------------------------------------------")
                return 0
    else:
        print("Please write y or n !")
        text_do_it()
text_do_it()