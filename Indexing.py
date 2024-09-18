

def create_index_low_level(key:int , Document:str , InvertedIndexDictionary ):
    Tokens  = set(Document.lower().split())
    for Token in Tokens: 
        if InvertedIndexDictionary.get(Token) == None:
            InvertedIndexDictionary[Token] = [int(key)]
        else:
            InvertedIndexDictionary[Token].append(int(key))            

def create_index(data):
    InvertedIndexDictionary = {} 
    for key , document in data.items():
        create_index_low_level(key , document , InvertedIndexDictionary)
        
    return InvertedIndexDictionary


                      



    