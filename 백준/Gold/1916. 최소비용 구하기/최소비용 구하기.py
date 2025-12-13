import heapq,sys
input = sys.stdin.readline

N = int(input())
M = int(input())
MAX = float('inf')
distance = [MAX] * (N + 1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u,v,cost = map(int,input().split())
    graph[u].append((v,cost))

src,dest = map(int,input().split())

def dijkstra(start):
    heap=[]
    heapq.heappush(heap,(0,start)) #비용, 노드
    distance[start] = 0
    while heap:
        cur_cost, cur_node = heapq.heappop(heap)
        if distance[cur_node] < cur_cost:
            continue
        for node in graph[cur_node]:
            cost = cur_cost+node[1]
            if distance[node[0]] > cost:
                distance[node[0]] = cost
                heapq.heappush(heap,(cost,node[0]))

# 다익스트라로 해야함
dijkstra(src)

print(distance[dest])