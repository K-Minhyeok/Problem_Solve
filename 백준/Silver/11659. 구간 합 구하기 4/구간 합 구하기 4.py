import sys
input = sys.stdin.readline

N,M = map(int,input().split())
nums = [int (x) for x in input().split()]
summation = [0]
tmp = 0

for num in nums:
    tmp += num
    summation.append(tmp)

for _ in range(M):
    s,e = map(int,input().split())
    print(summation[e]-summation[s-1])
