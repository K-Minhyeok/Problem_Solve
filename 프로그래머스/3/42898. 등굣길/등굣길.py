def solution(m, n, puddles):
    route = [[0]*(m+1) for _ in range(n+1)]
    route[1][1] = 1
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if [j,i] in puddles:
                continue
            route[i][j] += route[i-1][j] + route[i][j-1]
    
    return route[n][m]% 1000000007