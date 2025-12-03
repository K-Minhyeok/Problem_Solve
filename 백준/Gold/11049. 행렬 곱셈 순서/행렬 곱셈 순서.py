import sys
input = sys.stdin.readline

N = int(input())
mat = [[int (x) for x in input().split()]for _ in range(N)]
dp=[[0]*N for _ in range(N)]

# 앞 뒤 Mat 중에 작은 거
for cnt in range(N):  # 몇 개 셀건지
    for i in range(N-cnt-1): #어디서부터 셀건지
        j = cnt+i+1  # 어디까지 셀건지
        dp[i][j] = 2**31
        for k in range(i,j):
            dp[i][j] = min(dp[i][j],dp[i][k]+dp[k+1][j]+mat[i][0]*mat[k][1]*mat[j][1])

print(dp[0][-1])


