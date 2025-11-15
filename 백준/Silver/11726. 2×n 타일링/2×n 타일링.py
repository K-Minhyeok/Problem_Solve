N = int(input())
dp=[0]*N
dp[0]=1

if N >=2:
    dp[1]=2
    for i in range(2,N):
        dp[i]= dp[i-2]+dp[i-1]

print(dp[-1]%10007)