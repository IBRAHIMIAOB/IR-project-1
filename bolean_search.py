def boolean_search(query ):
    query = query.lower()
    import re, json
    with open("inverted2_index.json" , "r") as f :
        index = json.load(f)
    with open("data.json" , "r" ) as f  :
        data = json.load(f)

    and_parts = query.split('&')
    
    and_results = [index.get(part.strip(), set()) for part in and_parts]
    if len(and_results) > 1:
        and_result = and_results[0]
        for result_set in and_results[1:]:
            and_result = set(and_result).intersection(result_set)
    else:
        and_result = and_results[0]

    or_query = ' '.join(and_parts)  
    or_terms = re.split(r'\s+', or_query)
    or_results = set()
    
    for term in or_terms:
        if term in index:
            or_results.update(index[term])
    
    mapped = [data[str(ID)] for ID in or_results]


    return list(mapped)

x = boolean_search("samsung apple device")
for doc in x : 
    print(doc , end="\n\n\n\n")