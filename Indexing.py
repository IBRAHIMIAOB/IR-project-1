def create_index_low_level(key: int, Document: str, InvertedIndexDictionary):
    """
    This function processes a single document and updates the inverted index with the tokens found in that document.

    Args:
    - key (int): The unique identifier for the document.
    - Document (str): The text content of the document.
    - InvertedIndexDictionary (dict): The inverted index dictionary where terms are mapped to lists of document IDs.

    Returns:
    - None: The function modifies InvertedIndexDictionary in place.
    """
    # Split the document into unique tokens (words) in lowercase
    Tokens = set(Document.lower().split())

    # Update the inverted index with each token found in the document
    for Token in Tokens:
        if InvertedIndexDictionary.get(Token) is None:
            InvertedIndexDictionary[Token] = [
                int(key)
            ]  # Add the document ID to the new term
        else:
            InvertedIndexDictionary[Token].append(
                int(key)
            )  # Append the document ID to the existing term list


def create_index(data):
    """
    This function creates an inverted index from a given collection of documents.

    Args:
    - data (dict): A dictionary where keys are document IDs and values are the document text content.

    Returns:
    - dict: An inverted index mapping terms to lists of document IDs where the term occurs.
    """
    InvertedIndexDictionary = (
        {}
    )  # Initialize an empty dictionary for the inverted index

    # Process each document and update the inverted index
    for key, document in data.items():
        create_index_low_level(key, document, InvertedIndexDictionary)

    return InvertedIndexDictionary
