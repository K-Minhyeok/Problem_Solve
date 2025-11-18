import sys
sys.setrecursionlimit(100000)

N,M = map(int,input().split())
l = [[] for _ in range(N)]
visited = [False]*N
cnt =0

def search(i):
    visited[i]=True
    for j in range(len(l[i])):
        if not visited[l[i][j]]:
            visited[l[i][j]]=True
            search(l[i][j])

        

for _ in range(M):
    a,b = map(int,input().split())
    l[a-1].append(b-1)
    l[b-1].append(a-1)


for i in range(N):
    if not visited[i] :
        search(i)
        cnt+=1

print(cnt)