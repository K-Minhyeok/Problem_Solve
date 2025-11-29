def backtracking(i):
    if len(res) == M:
        print(*res)
        return
    
    for i in range(1,N+1):
            res.append(i)
            backtracking(i)
            res.pop()



N,M = map(int,input().split())
res = []

backtracking(1)
