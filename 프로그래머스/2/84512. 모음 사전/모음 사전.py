from itertools import product

def solution(word):
    alpha = ['A','E','I','O','U']
    pair =[]
    for i in range(1,len(alpha)+1):
        data = list(product(alpha,repeat=i))
        print(data)
        for j in data:
                tmp = "".join(j)
                print(j)
                pair.append(tmp)
    pair.sort()
    
    for i,w in enumerate(pair):
        if len(w) == len(word) and w == word:
            return i+1