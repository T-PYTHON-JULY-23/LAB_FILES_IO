
import json
from datetime import datetime
datestring = datetime.now()
print(datestring)
json_string = {"to do": 'go to gym' , "date": 'date' , "done " : True }
file = open("jsonfile.json",'w')
json.dump(json_string,file)
file.close



    