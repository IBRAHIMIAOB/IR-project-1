from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
import time , datetime
import json
def create_index(key:int , Document:str , InvertedIndexDictionary:dict):
    Tokens = tokenizer.tokenize(Document)
    for Token in Tokens: 
        if InvertedIndexDictionary.get(Token) == None:
            InvertedIndexDictionary[Token] = [key]
        else:
            insert_To_sorted_list_and_keep_sorted(InvertedIndexDictionary[Token] , key)
            

def insert_To_sorted_list_and_keep_sorted(LIST:list, key:int):
    for i in range(len(LIST)):
        if LIST[i] > key:
            LIST.insert(i , key)
            return
    LIST.insert(len(LIST), key)
    
inverted_index = {}     
    


with open("data.json" , "r") as f:
    data:dict = json.load(f)
    
for key  , document in data.items():
    if int(key) % 1000 == 0 :
        print(f"{key} : {datetime.datetime.now()}")
    create_index(key , document , inverted_index)
    
with open("inverted_index.json" , "w") as f : 
    json.dump(inverted_index , f , indent=0)
    
    
            
            



    