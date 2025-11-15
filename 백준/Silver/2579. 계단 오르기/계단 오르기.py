n = int(input())
stair =[int(input()) for _ in range(n)]
dp=[0]*n
if len(stair) <=2 : 
    print(sum(stair))
else:
    dp[0] = stair[0]
    dp[1] = stair[0]+stair[1]

    for i in range(2,n):
        # 각 레벨별로 가는 데에 최대값을 저장한다.
        dp[i] = max(dp[i-3]+stair[i-1]+stair[i],dp[i-2]+stair[i])

    print(dp[-1])