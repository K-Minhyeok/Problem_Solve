def solution(sizes):
    #가로에는 한 쌍 중에 큰 애들을 넣어둔다.
    #세로에는 한 쌍 중에 작은 애들은 넣어둔다.
    
    #가로 : 큰 애들 중에 가장 큰 애
    #세로 : 작은 애들 중에 가장 큰 애
    max_len =-1
    max_wid =-1
    
    for size in sizes:
        width = max(size)
        length = min(size)
        
        max_wid = max(width,max_wid)
        max_len = max(length,max_len)
    
    return max_len*max_wid
    
    return max_w*max_h
