import sys
input = sys.stdin.readline
N,M = map(int,input().split())

l = [[int(x) for x in input().split()]for _ in range(N)]
dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + l[i-1][j-1]
# 마지막에 본인 더한 거임


for _ in range(M):
    si, sj, ei, ej = map(int, input().split())
    res = dp[ei][ej] - dp[si-1][ej] - dp[ei][sj-1] + dp[si-1][sj-1]
    print(res)