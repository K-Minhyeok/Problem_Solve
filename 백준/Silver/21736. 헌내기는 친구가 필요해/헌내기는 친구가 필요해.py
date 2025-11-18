import sys
from collections import deque
input = sys.stdin.readline
canmove = [(1,0),(0,1),(-1,0),(0,-1)]
queue = deque()
cnt= 0
si,sj=0,0

N,M = map(int,input().split())

visited = [[False]*M for _ in range(N)]

l = [input().strip() for _ in range(N)]

for i in range(N):
    for j in range(M):
        if l[i][j] == "I":
            si,sj = i,j

queue.append((si,sj))
visited[si][sj]=True

while queue:
    i,j = queue.popleft()
    if l[i][j] == "P":
        cnt+=1
    for wi,wj in canmove:
        ti, tj = wi+i , wj+j
        if 0<=ti<N and 0<=tj<M and not visited[ti][tj] and l[ti][tj]!="X":
            queue.append((ti,tj))
            visited[ti][tj]=True
if cnt ==0 :
    print("TT")
else : 
    print(cnt)