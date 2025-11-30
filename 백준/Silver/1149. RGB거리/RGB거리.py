N = int(input())

l = [[int(x) for x in input().split()]for _ in range(N)]

dp = l.copy()
for i in range(1,N):
    dp[i][0] += min(dp[i-1][1],dp[i-1][2])
    dp[i][1] += min(dp[i-1][0],dp[i-1][2])
    dp[i][2] += min(dp[i-1][0],dp[i-1][1])

print(min(dp[N-1]))