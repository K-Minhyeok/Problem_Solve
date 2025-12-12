import sys
input = sys.stdin.readline

N,M = map(int,input().split())
left_max = -1
right_min= 10**9

for _ in range(N):
    start,end,y = map(int,input().split())
    left_max = max(left_max,start)
    right_min = min(right_min,end)

for _ in range(M):
    x = int(input())
    print(max(left_max-x,x-right_min,0))