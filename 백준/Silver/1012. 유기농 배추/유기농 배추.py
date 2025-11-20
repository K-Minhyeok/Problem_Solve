from collections import deque

move = [(1,0),(0,1),(-1,0),(0,-1)]
T = int(input())


for _ in range(T):
    M,N,K= map(int,input().split())
    board = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    cnt=0
    queue = deque()
    for p in range(K):
        i,j =map(int,input().split())
        board[j][i] = 1
    
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and board[i][j]==1:
                cnt+=1
                queue.append((i,j))
                visited[i][j] = True
                while queue:
                    bi,bj = queue.popleft()
                    for wi,wj in move:
                        ci ,cj = bi+wi,bj+wj
                        if 0<=ci<N and 0<=cj<M and not visited[ci][cj] and board[ci][cj]==1:
                            queue.append((ci,cj))
                            visited[ci][cj]=True
    print(cnt)
