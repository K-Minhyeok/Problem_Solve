def solution(sizes):
    #가로에는 한 쌍 중에 큰 애들을 넣어둔다.
    #세로에는 한 쌍 중에 작은 애들은 넣어둔다.
    
    #가로 : 큰 애들 중에 가장 큰 애
    #세로 : 작은 애들 중에 가장 큰 애
    max_w = -1
    max_h = -1
    
    for pair in sizes:
        w ,h = max(pair) , min(pair)
        max_w = max(max_w,w)
        max_h = max(max_h,h)
    
    return max_w*max_h
