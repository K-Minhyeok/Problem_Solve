from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
board = [[int (x) for x in input().split()] for _ in range(N)]
visited = [[False]*M for _ in range(N)]
move = [(1,0),(0,1),(-1,0),(0,-1)]
queue = deque()
for i in range(N):
    for j in range(M):
        if board[i][j]==2:
            start_x,start_y = j,i

queue.append((start_y,start_x,0))
visited[start_y][start_x]=True

while queue:
    y,x,cnt = queue.popleft()
    board[y][x] = cnt
    for i,j in move:
        nx,ny = x+i,y+j  
        if 0<=nx<M and 0<=ny<N and board[ny][nx]==1 and not visited[ny][nx]:
            visited[ny][nx] = True
            queue.append((ny,nx,cnt+1))

for i in range(N):
    for j in range(M):
        if board[i][j]==1 and not visited[i][j]:
            board[i][j] = -1
        print(board[i][j],end=" ")
    print()