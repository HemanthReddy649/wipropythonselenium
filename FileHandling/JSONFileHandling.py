#JSON JAVASCRIPT OBJECT NOTATION
#FORM OF OBJECTS FORMAT

import json
with open("C://Users//thiru//PycharmProjects//PythonAdvanceProject//DataFormats//employee.json",'r') as file:
    data=json.load(file)
print(data)
print(data["name"])
#read the json file -load
with open("C://Users//thiru//PycharmProjects//PythonAdvanceProject//DataFormats//nestedemployee.json",'r') as file:
    data=json.load(file)
email=data["user"]["profile"]["email"]
print(email)



#writing to json file -dump

data={
  "name": "Harsha",
  "role": "Tester",
  "experience": 5,
  "skills": ["Python", "Automation", "API"]
}

with open ("C://Users//thiru//PycharmProjects//PythonAdvanceProject//DataFormats//writejson.json",'w') as file:
    json.dump(data,file)

    #update or modify the json file

    #read the json file
    #modify the data
    #write it back to the file
with open("C://Users//thiru//PycharmProjects//PythonAdvanceProject//DataFormats//updatejson.json",'r') as file:
    data=json.load(file)

    #update the value
data["experience"]=6
#write back

#xxxxxx