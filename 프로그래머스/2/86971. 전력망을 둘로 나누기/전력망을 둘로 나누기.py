from collections import deque,defaultdict

def dfs(K,tree,visited):
    visited[K] = True
    cnt=1
    
    for node in tree[K]:
        if not visited[node]:
            cnt += dfs(node,tree,visited)
    return cnt
        
def solution(n, wires):
    d = [[] for _ in range(n+1) ]
    answer = 9999
    for a,b in wires:
        d[a].append(b)
        d[b].append(a)
    
    for a,b in wires:
        visited = [False]*(n+1)

        d[a].remove(b)
        d[b].remove(a)
        # a 연결 수 , b 연결 수
        edge_a = dfs(a,d,visited)
        edge_b = dfs(b,d,visited)

        answer = min(answer,abs(edge_a - edge_b))
        
        d[a].append(b)
        d[b].append(a)      
        
    return answer
