import sys
from collections import deque
input = sys.stdin.readline
MAX = 10**5

N,M = map(int,input().split())
ground = [-1]*(MAX+1)
queue = deque()
queue.append(N)
ground[N] = 0

while queue:
    x= queue.popleft()
    if x==M :
        print(ground[x])
        break
    for i in (x+1,x-1,x*2):
        if 0<=i<=MAX and ground[i] ==-1:
            ground[i]=ground[x]+1
            queue.append(i)
