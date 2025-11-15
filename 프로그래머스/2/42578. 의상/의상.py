import math
def solution(clothes):
    options = dict()
    result = 1

    for pair in clothes:
        if pair[1] in options:
            options[pair[1]] +=1
        else :
            options[pair[1]] =1            

    for count in options.values():
        result *= count+1
        
    return result-1
        
        
    
    
    

    print(count)
    