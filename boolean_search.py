import json
def boolean_search(inverted_index , data , expr):
    expr = expr.lower()
    temp = expr.replace("&" , " ").replace(")" , " ").replace("(" , " ")
    listOfWords = temp.split()
   
    global_values = {}
    for Word in listOfWords:
        docList = inverted_index.get(Word) or {}
        global_values[Word] = set(docList)
    
    expr = expr.replace(' ' , '|')
    expr = expr.replace('&', '&') 
    try:
        
       result = eval(expr ,global_values )
       
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        return list()
    
    return [data.get(term) for term in result]   
    
