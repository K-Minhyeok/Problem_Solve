from collections import defaultdict,deque

N = int(input())
tree = defaultdict(list)
queue = deque()
queue.append(1)
parent = [0]*(N+1)
for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

while queue:
    node = queue.popleft()
    child = tree[node]
    for i in child:
        if parent[i] ==0:
            parent[i] = node
            queue.append(i)


for i in range(2,N+1):
    print(parent[i])