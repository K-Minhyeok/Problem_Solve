T = int(input())
dp=[0]*11
dp[0]=1
dp[1]=2
dp[2]=4
for j in range(3,11):
        dp[j]= dp[j-3]+dp[j-2]+dp[j-1]

for i in range(T):
    N = int(input())
    print(dp[N-1])

#1 나타내는 법 1                                         = 1
#2 나타내는 법 1+1 , 2                                   = 2
#3 나타내는 법 1+1+1, 2+1, 1+2, 3                        = 4
#4 나타내기 1+1+1+1 , 1+1+2, 1+2+1,2+1+1, 2+2, 1+3, 3+1 = 7
