from collections import deque

def search(i,j):
    queue.append((i,j,0))
    visited[i][j][0] = 1
    while queue:
        i,j,broke = queue.popleft()
        if (i,j) == (N-1,M-1):
            return visited[i][j][broke]
        
        for mi,mj in mij:
            ni ,nj = mi+i , mj+j
            if 0<=ni<N and 0<=nj<M :
                if l[ni][nj] == 1 and broke == 0 and visited[ni][nj][1] == 0:
                    visited[ni][nj][1] = visited[i][j][0] + 1
                    queue.append((ni,nj,1))

                elif l[ni][nj] == 0 and visited[ni][nj][broke] == 0:
                    visited[ni][nj][broke] = visited[i][j][broke] + 1
                    queue.append((ni,nj,broke))
    
    return -1

queue = deque()
N,M = map(int,input().split())
l = [list(map(int,input().rstrip())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
mij = [(1,0),(0,1),(-1,0),(0,-1)]
visited[0][0][0] = 1
print(search(0,0))