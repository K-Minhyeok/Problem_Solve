def backtracking():
    check = 0
    if len(res) == m:
        print(*res)
        return
    for i in range(n):
        if check != l[i] and visited[i] == 0:
            res.append(l[i])
            visited[i] = 1
            check = l[i]
            backtracking()
            res.pop()
            visited[i] = 0


n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
visited = [0] * n
res = []
backtracking()