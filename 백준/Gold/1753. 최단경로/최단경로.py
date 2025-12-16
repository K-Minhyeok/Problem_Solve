import sys
import heapq

def dijkstra(src):
    heap = []
    heapq.heappush(heap,(0,src))
    distance[src] = 0
    while heap:
        w,v =  heapq.heappop(heap)
        if w> distance[v]:
            continue
        for adj in graph[v]:
            cost = w+adj[1]
            if cost < distance[adj[0]]:
                distance[adj[0]] = cost
                heapq.heappush(heap,(cost,adj[0]))

input = sys.stdin.readline
MAX = float('inf')
V , E = map(int,input().split())
graph = [[]*V for _ in range(V)]
distance = [MAX]*V 
start = int(input())

for i in range(E):
    src,to,weight = map(int,input().split())
    graph[src-1].append((to-1,weight))

dijkstra(start-1)

for d in distance: 
    if d == float('inf'):
        print("INF")
    else:
        print(d)