N = int(input())
info =[]
dp = [0]*(N+1)
# 며칠 기다려야 하는지, 현재까지 최대 이익 얼마인지
 
for i in range(N):
    T,P = map(int,input().split())
    info.append((T,P))

#dp[0] : (3,10)
#dp[1] : (5,20)
#dp[2] : (5,20)
#dp[3] : (1,30) .. 며칠 기다려야하는지 ,1일이랑 4일 더한 profit 
#dp[4] : (2,45) .. 2일 기다려야함 , 1,4,5 더했음 if 지금 기다려야하는 게 최종 날짜에 안 닿는지
#dp[5] : 

for i in range(N-1,-1,-1):
    if info[i][0]+i > N: 
        dp[i] =dp[i+1]
    else :
        dp[i] = max(dp[i+1],info[i][1]+dp[i+info[i][0]])

print(dp[0])

    