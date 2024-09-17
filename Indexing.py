
import time , datetime
startTime = time.perf_counter()
import json
def create_index(key:int , Document:str , InvertedIndexTrie ):
    Tokens  :list[int]= set(Document.split())
    for Token in Tokens: 
        if InvertedIndexTrie.get(Token) == None:
            InvertedIndexTrie[Token] = [int(key)]
        else:
            InvertedIndexTrie[Token].append(int(key))            

def insert_To_sorted_list_and_keep_sorted(LIST:list, key:int):
    for i in range(len(LIST)):
        if LIST[i] > key:
            LIST.insert(i , key)
            return
    LIST.insert(len(LIST), key)
    
InvertedIndexTrie = {} 
    


with open("data.json" , "r") as f:
    data:dict = json.load(f)
    
for key  , document in data.items():
    create_index(key , document , InvertedIndexTrie)
    
with open("inverted2_index.json" , "w") as f : 
    json.dump(InvertedIndexTrie , f , indent=1)

print(time.perf_counter() - startTime , end="s")
    
                      



    