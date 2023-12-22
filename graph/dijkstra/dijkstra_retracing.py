from heapq import *
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    heap = []
    heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        dist, now = heappop(heap)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(heap, (cost, i[0]))
                path[i[0]] = []
                for p in path[now]:
                    path[i[0]].append(p)
                path[i[0]].append(i[0])

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())
path = [[] for _ in range(n+1)]
path[start].append(start)

dijkstra(start)
print(distance[end])
print(len(path[end]))
print(' '.join(map(str, path[end])))
