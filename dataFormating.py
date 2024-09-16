#since the data does not have unique ID That determine the specific entity 
# and also the data is not formatted well ... this file is in charge of fix all these problems

import json 
with open("data.txt"  , "r" ) as f :
    News = f.readlines()

formatedData = {}
i= 0
for New in News:
    i= i+1
    New = json.loads(New) 
    
    category = New.get("category") or " "
    authors = New.get("authors") or " "
    headline =  New.get("headline") or " "
    short_description = New.get("short_description") or " "
    date = New.get("date") or " "
    link = New.get("link") or " "
    Text = " ".join([category , authors , headline , short_description , date , link ])
    formatedData[i] = Text
    
    
with open("data.json" , "w") as f:
    json.dump(formatedData , f , indent=1)
    
#New data formatted as key of increasing integer and one line contains [category , authors , headline , short_description , date , link ]