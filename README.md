
# Boolean Search Project

## Project Overview

This project implements a Boolean Search engine using Python. It involves the creation of an inverted index for efficient search and the ability to evaluate complex Boolean expressions using terms like `AND`, `OR`, and parentheses. The data is formatted, indexed, and queried to enable dynamic Boolean searches.

---

## Files in the Project

### 1. **indexing.py**
Contains functions for building the inverted index:
- **`create_index_low_level(key, Document, InvertedIndexDictionary)`**: Processes a single document and updates the inverted index.
- **`create_index(data)`**: Creates an inverted index for a collection of documents.

### 2. **boolean_search.py**
Implements the Boolean search logic:
- **`boolean_search(inverted_index, data, expr)`**: Executes a Boolean query using the inverted index and returns matching documents.

### 3. **dataFormatting.py**
Formats the raw data into a structured JSON format:
- **`FormatData()`**: Reads raw data from `data.txt`, assigns unique IDs, and creates a structured JSON file `data.json`.

### 4. **runMe.ipynb**
A Jupyter Notebook that:
- Formats the data using `FormatData()`.
- Creates the inverted index using `create_index()`.
- Runs and tests Boolean queries using `boolean_search()`.

---

## Features

1. **Inverted Index Creation**:
   - Efficient indexing of documents by terms.
   - Handles large datasets with ease.

2. **Boolean Query Support**:
   - Evaluates expressions with `AND` (`&`), `OR` (space), and parentheses for grouping.
   - Case-insensitive matching.

3. **Data Formatting**:
   - Transforms raw unstructured data into a structured JSON format.

4. **Performance Measurement**:
   - Measures execution time of queries for optimization insights.

---

## How to Use

### Step 1: Format Data
Run the `FormatData()` function to structure the raw data into a JSON file:
```python
from dataFormatting import FormatData

Data = FormatData()
```

### Step 2: Create Inverted Index
Generate the inverted index using the formatted data:
```python
from indexing import create_index

inverted_index = create_index(Data)
```

### Step 3: Perform a Boolean Search
Run a Boolean query on the data:
```python
from boolean_search import boolean_search

query = "global & warming"  # Example query
results = boolean_search(inverted_index, Data, query)

for result in results:
    print(result)
```

### Step 4: Measure Performance
Measure the time taken to process a query:
```python
import time

start_time = time.perf_counter_ns()
results = boolean_search(inverted_index, Data, "global & warming")
elapsed_time = time.perf_counter_ns() - start_time

print(f"Time taken: {elapsed_time} ns")
```

---

## Query Guidelines

1. **Spaces (` `)**: Represent the `OR` operation.
2. **Ampersand (`&`)**: Represents the `AND` operation.
3. **Parentheses (`(` and `)`)**: Used for grouping terms.
4. Avoid leading or trailing spaces in queries.
5. Ensure no spaces exist before or after `&` or parentheses.

---

## Example Queries

| Query               | Meaning                                   |
|---------------------|-------------------------------------------|
| `global warming`    | Documents containing "global" OR "warming". |
| `global & warming`  | Documents containing both "global" AND "warming". |
| `(global & warming) | energy` | Documents containing both "global" AND "warming", OR containing "energy". |

---

## Prerequisites

- Python 3.6+
- Basic knowledge of Boolean logic and text search.

---

## References

- `data.txt`: Raw data file used for input.
- `data.json`: Formatted data created by `FormatData()`.
```

Let me know if further adjustments are needed! 😊
