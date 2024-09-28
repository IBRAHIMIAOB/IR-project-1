import json


# since the data does not have unique ID That determine the specific entity
# and also the data is not formatted well ... this file is in charge of fix all these problems


def FormatData():
    """
    This function reads raw news data from a text file, formats it into a structured JSON format,
    and writes the formatted data to a new JSON file.

    Returns:
    - dict: A dictionary containing the formatted news data with unique IDs as keys.
    """
    with open("data.txt", "r") as f:
        News = f.readlines()  # Read all lines from the data file

    formattedData = {}
    i = 0  # Initialize a counter for unique document IDs

    # Process each line of the news data
    for New in News:
        i += 1
        New = json.loads(New)  # Parse the JSON data

        # Extract relevant fields, providing a default empty string if any field is missing
        category = New.get("category", " ")
        authors = New.get("authors", " ")
        headline = New.get("headline", " ")
        short_description = New.get("short_description", " ")
        date = New.get("date", " ")
        link = New.get("link", " ")

        # Combine all fields into a single text block for the document
        Text = "\n".join([category, authors, headline, short_description, date, link])
        formattedData[i] = (
            Text  # Assign the formatted text to the dictionary with a unique ID
        )

    # Save the formatted data to a JSON file
    with open("data.json", "w") as f:
        json.dump(formattedData, f, indent=1)

    return formattedData


# New data formatted as key of increasing integer and one line contains [category , authors , headline , short_description , date , link ]
