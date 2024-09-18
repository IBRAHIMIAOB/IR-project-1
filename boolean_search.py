def boolean_search(query):
    query = query.lower()
    import re, json

    with open("inverted2_index.json", "r") as f:
        index = json.load(f)

    with open("data.json", "r") as f:
        data = json.load(f)

    # Split query on AND operator and process each part
    and_parts = query.split('&')
    
    # Handle AND operator: Intersection of terms within each AND part
    and_results = [set(index.get(part.strip(), set())) for part in and_parts]
    if len(and_results) > 1:
        and_result = and_results[0]
        for result_set in and_results[1:]:
            and_result = and_result.intersection(result_set)
    else:
        and_result = and_results[0]

    # Now handle the OR operation only on the AND result
    or_query = ' '.join(and_parts)  # Join back into a single query string for OR operation
    or_terms = re.split(r'\s+', or_query)
    
    # Keep only the terms from the original OR terms that are present in the AND result
    or_results = set()
    for term in or_terms:
        if term in index:
            or_results.update(index[term])

    # Now intersect OR results with AND result, so AND takes priority
    final_results = or_results.intersection(and_result)

    # Map document IDs to actual data
    mapped = [data[str(ID)] for ID in final_results]

    return list(mapped)

# Test with the search query
x = boolean_search("apple&stock")
for doc in x:
    print(doc, end="\n\n\n\n")
