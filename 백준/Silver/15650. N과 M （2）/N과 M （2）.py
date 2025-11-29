def backtracking(i):
    if len(res) == M:
        print(*res)
        return
    
    for i in range(i,N+1):
        if i not in res:
            res.append(i)
            backtracking(i+1)
            res.pop()

N,M = map(int,input().split())
res = []

backtracking(1)
