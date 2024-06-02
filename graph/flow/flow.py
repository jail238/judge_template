from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

n, p = map(int, input().split())
cap = [[0 for _ in range(n+1)] for _ in range(n+1)]
flow = [[0 for _ in range(n+1)] for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(p):
    a, b, c = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    cap[a][b] = c

total_flow, s, t = 0, 1, 2

while True:
    prev = [-1 for _ in range(n+1)]
    q = deque()
    q.append(s)
    while q and prev[t] == -1:
        now = q.popleft()
        for nxt in graph[now]:
            if cap[now][nxt] - flow[now][nxt] > 0:
                if prev[nxt] == -1:
                    q.append(nxt)
                    prev[nxt] = now
                    if nxt == t: break
    if prev[t] == -1: break
    
    f, i = INF, t
    while i != s:
        f = min(f, cap[prev[i]][i]-flow[prev[i]][i])
        i = prev[i]
    
    i = t
    while i != s:
        flow[prev[i]][i] += f
        flow[i][prev[i]] -= f
        i = prev[i]
    total_flow += f
print(total_flow)
