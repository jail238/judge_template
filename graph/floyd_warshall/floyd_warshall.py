import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c # 양방향일 때 추가

for k in range(1, n+1):
    graph[k][k] = 0
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
