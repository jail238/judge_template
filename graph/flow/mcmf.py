from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
cap = [[0 for _ in range(n+m+3)] for _ in range(n+m+3)] # 용량
flow = [[0 for _ in range(n+m+3)] for _ in range(n+m+3)] # 유량
cost = [[0 for _ in range(n+m+3)] for _ in range(n+m+3)] # 비용
graph = [[] for _ in range(n+m+3)]

# write graph information
total_flow, total_cost, src, sink = 0, 0, 1, 2

while True:
    prev = [-1 for _ in range(n+m+3)]
    dist = [INF for _ in range(n+m+3)]
    inq = [False for _ in range(n+m+3)]
    q = deque(); q.append(src)
    dist[src] = 0; inq[src] = True
    
    while q:
        now = q.popleft()
        inq[now] = False
        for nxt in graph[now]:
            if cap[now][nxt] - flow[now][nxt] > 0 and cost[now][nxt]+dist[now] < dist[nxt]:
                dist[nxt] = dist[now]+cost[now][nxt]
                prev[nxt] = now
                if not inq[nxt]:
                    q.append(nxt)
                    inq[nxt] = True

    if prev[sink] == -1: break
    f, i = INF, sink
    while i != src:
        f = min(f, cap[prev[i]][i]-flow[prev[i]][i])
        i = prev[i]
    i = sink
    while i != src:
        total_cost += f*cost[prev[i]][i]
        flow[prev[i]][i] += f
        flow[i][prev[i]] -= f
        i = prev[i]
    total_flow += f

print(total_flow)
print(total_cost)
