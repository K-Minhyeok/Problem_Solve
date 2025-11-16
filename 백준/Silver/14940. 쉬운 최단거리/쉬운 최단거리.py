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
            start_x,start_y = i,j

queue.append((start_x,start_y,0))
visited[start_x][start_y]=True

while queue:
    x,y,cnt = queue.popleft()
    board[x][y] = cnt
    for i,j in move:
        nx,ny = x+i,y+j  
        if 0<=nx<N and 0<=ny<M and board[nx][ny]==1 and not visited[nx][ny]:
            visited[nx][ny] = True
            queue.append((nx,ny,cnt+1))

for i in range(N):
    for j in range(M):
        if board[i][j]==1 and not visited[i][j]:
            board[i][j] = -1
        print(board[i][j],end=" ")
    print()