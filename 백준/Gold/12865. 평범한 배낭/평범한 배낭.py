N , K = map(int,input().split())
bag =[]
dp = [[0]*(N+1) for _ in range(K+1)]
for _ in range(N):
    W , V = map(int,input().split())
    bag.append((W,V))

for k in range(1,K+1):
    # 가방이 무게 k만큼 감당 가능할 떄(0인 경우는 없으니 편의상 1부터로 잡았다.)
    for i in range(1,N+1):
        w,v = bag[i-1]
        if w <=k:
            dp[k][i] = max(dp[k][i-1],v+dp[k-w][i-1])
        else:
            dp[k][i] = dp[k][i-1]

    # for i in dp:
    #     print(*i)
    # print("------")
print(dp[K][N])