from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
import pygtrie
import time , datetime
import json
def create_index(key:int , Document:str , InvertedIndexTrie : pygtrie.CharTrie):
    Tokens = tokenizer.tokenize(Document)
    for Token in Tokens: 
        if not InvertedIndexTrie.has_key(Token):
            InvertedIndexTrie[Token] = [key]
        else:
            insert_To_sorted_list_and_keep_sorted(InvertedIndexTrie[Token] , key)
            

def insert_To_sorted_list_and_keep_sorted(LIST:list, key:int):
    for i in range(len(LIST)):
        if LIST[i] > key:
            LIST.insert(i , key)
            return
    LIST.insert(len(LIST), key)
    
InvertedIndexTrie = pygtrie.CharTrie()    
    


with open("data.json" , "r") as f:
    data:dict = json.load(f)
    
for key  , document in data.items():
    if int(key) % 1000 == 0 :
        print(f"{key} : {datetime.datetime.minute()}")
    create_index(key , document , InvertedIndexTrie)
    
with open("inverted_index.json" , "w") as f : 
    json.dump(InvertedIndexTrie , f , indent=0)
    
    
            
            



    