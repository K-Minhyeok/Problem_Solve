N = int(input())
l = [[int(x) for x in input().split()]for _ in range(N)]
dp = l.copy()

for i in range(1,N):
    for j in range(len(l[i])):
        if j == 0:
            dp[i][j]+= dp[i-1][0]
        elif j == len(l[i])-1 :
            dp[i][j]+= dp[i-1][j-1]
        else:
            dp[i][j]+= max(dp[i-1][j-1],dp[i-1][j])

print(max(dp[len(l)-1])) 