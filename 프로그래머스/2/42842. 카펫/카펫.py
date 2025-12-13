def solution(brown, yellow):
    total = brown+yellow
    possible = []
    
    for i in range(1,total//2):
        if total %i == 0:
            possible.append((total//i,i))
    
    for width,length in possible:
        edge = (width*2) + (length*2) - 4
        if edge == brown :
            return [width,length]
        
