from collections import deque

move = [(1,0),(0,1),(-1,0),(0,-1)]
M,N = map(int,input().split())
board = [[int(x) for x in input().split()]for _ in range(N)]
queue = deque()

for j in range(N):
    for i in range(M):
        if board[j][i]==1:
            queue.append((j,i,1))
            board[j][i] = 1
total = 0
done = True

while queue:
    j,i,cnt = queue.popleft()
    for wj,wi in move:
        if 0<=wj+j <N and 0<= wi+i< M and board[wj+j][wi+i] ==0:
            board[wj+j][wi+i] = cnt 
            queue.append((wj+j,wi+i,cnt+1))
            total = max(cnt,total)
    

for j in range(N):
    for i in range(M):
        if board[j][i]==0:
            done = False
            break

if done:
    print(total)
else:
    print(-1)