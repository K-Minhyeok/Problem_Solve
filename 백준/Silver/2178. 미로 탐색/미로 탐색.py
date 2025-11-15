from collections import deque
import sys
input = sys.stdin.readline
move = [(1,0),(0,1),(-1,0),(0,-1)]

N,M = map(int,input().split())

board = [[int (x) for x in input().strip()]for _ in range(N)]
queue = deque()
visited = [[False]*M for _ in range(N)]
visited[0][0]=True
queue.append((0,0,1))

while queue :
    x,y,cnt = queue.popleft()
    if x == N-1 and y == M-1 :
        print(cnt)
        break
    else :
        for i,j in move:
            xi,yi = x+i,y+j
            if 0 <= xi < N  and 0<=yi < M and board[xi][yi] ==1 and not visited[xi][yi]:
                queue.append((xi,yi,cnt+1))
                visited[xi][yi]=True
