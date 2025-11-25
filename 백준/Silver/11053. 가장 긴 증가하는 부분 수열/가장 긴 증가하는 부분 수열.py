N = int(input())
nums = [int(x) for x in input().split()]
dp = [1]*N

for i in range(1,N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))