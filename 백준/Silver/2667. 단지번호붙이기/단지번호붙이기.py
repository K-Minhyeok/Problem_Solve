from collections import deque
move = [(1,0),(0,1),(-1,0),(0,-1)]

def search(i,j):
    queue = deque()
    queue.append((i,j))
    cnt=1
    while queue :
        i,j = queue.popleft()
        for wi,wj in move:
            ci ,cj = i+wi , j+wj
            if 0<=ci<N and 0<=cj<N and board[ci][cj] =='1' and not visited[ci][cj]:
                queue.append((ci,cj))
                visited[ci][cj] = True
                cnt+=1
    return cnt
    

N = int(input())
board = [input().strip() for _ in range(N)]
visited = [[False]*N for _ in range(N)]
area = 0
res = []
for i in range(N):
    for j in range(N):
        if board[i][j] == '1' and not visited[i][j]:
            visited[i][j] = True
            res.append(search(i,j))
            area+=1
            
res.sort()
print(area)
for i in res:
    print(i)
