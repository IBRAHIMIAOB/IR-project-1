import json


def boolean_search(inverted_index, data, expr):
    """
    This function performs a boolean search on the indexed data using AND/OR operators.

    Args:
    - inverted_index (dict): The inverted index containing terms and the list of document IDs where they appear.
    - data (dict): The original dataset containing document text.
    - expr (str): The search query containing terms with AND (&) and OR (space) operators.

    Returns:
    - list: A list of documents matching the boolean search query.
    """
    expr = (
        expr.lower()
    )  # Convert the search query to lowercase for case-insensitive matching
    temp = expr.replace("&", " ").replace(")", " ").replace("(", " ")
    listOfWords = temp.split()  # Extract all individual search terms

    # Dictionary to hold the sets of document IDs for each term in the query
    global_values = {}
    for Word in listOfWords:
        docList = inverted_index.get(Word) or {}
        global_values[Word] = set(
            docList
        )  # Store the document IDs as a set for faster operations

    # Replace spaces with OR operator and leave the & operator intact
    expr = expr.replace(" ", "|").replace("&", "&")

    try:
        # Evaluate the boolean expression using the sets of document IDs
        result = eval(expr, global_values)
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        return list()

    # Return the list of documents that match the query
    return [data.get(term) for term in result]
