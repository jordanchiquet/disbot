import wikipedia
import re

def wikipediaSearch(query: str):
    print("wikipediaSearch started with query: [" +
    query + "]")    
    query = re.sub(r'[()]', '', query)
    try:
        #result_type is meant to establish if I got a page, a disambig, or a right out error. I'm sure there's one word I just can't think of. 
        result_type = 0
        result = (wikipedia.page(query))
    except wikipedia.exceptions.DisambiguationError as e:
        result_type = 1
        result = e.options
    except wikipedia.exceptions.PageError:
        result_type = 2
        result = None
    print(f"exiting wikipediaSearch for {query} with result_type: {result_type} and result: {result}")
    return(result_type, result)
