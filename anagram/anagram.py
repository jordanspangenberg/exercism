import collections
def find_anagrams(word, candidates):
    sortedWord = sorted(list(word.lower()))
    result = []
    for item in candidates:
        if (sorted(list(item.lower())) == sortedWord 
        and word.lower() != item.lower() 
        and len(word) == len(item)):
            result.append(item)
    return result
                


    
