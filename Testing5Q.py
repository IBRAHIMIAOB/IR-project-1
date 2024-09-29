from dataFormatting import FormatData
from Indexing import create_index
from boolean_search import boolean_search
from time import perf_counter_ns
import matplotlib.pyplot as plt

query = ["samsung&apple" , "super&sad" , "paint" , "program" , "war" , "Global&Warming"]


data = FormatData()
index= create_index(data)
arr=  []
for q in query:
    start = perf_counter_ns()
    array = boolean_search(index , data , q)
    
    amount = len(array)
    totalTime = (perf_counter_ns()-start) 
    arr.append(totalTime)
    

plt.title("Boolean search performance")
plt.xlabel("Query")
plt.ylabel("Time in ns")
plt.bar(query , arr)
plt.show()


    