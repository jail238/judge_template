from heapq import *
import sys
input = sys.stdin.readline
INF = int(1e6)

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

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c)) # 양방향일 때 추가

start = int(input())
dijkstra(start)
