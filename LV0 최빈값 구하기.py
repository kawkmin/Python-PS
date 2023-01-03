from collections import Counter

def solution(array):
    counter_most=Counter(array).most_common()
    
    if len(counter_most)>1:
        if counter_most[0][1] == counter_most[1][1]: 
            return -1
    return counter_most[0][0]