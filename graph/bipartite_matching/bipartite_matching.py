from collections import deque
import sys
input = sys.stdin.readline
MAX = 10101
INF = int(1e9)

a_lvl, b_lvl = [-1 for _ in range(MAX)], [-1 for _ in range(MAX)]
dist = [INF for _ in range(MAX)]
visited = [False for _ in range(MAX)]
graph = [[] for _ in range(MAX)]

def bfs():
    q = deque()
    for i in range(MAX):
        if not visited[i]:
            dist[i] = 0
            q.append(i)
        else: dist[i] = INF

    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if b_lvl[nxt] != -1 and dist[b_lvl[nxt]] == INF:
                dist[b_lvl[nxt]] = dist[now]+1
                q.append(b_lvl[nxt])

def dfs(now):
    for nxt in graph[now]:
        if b_lvl[nxt] == -1 or (dist[b_lvl[nxt]] == dist[now]+1 and dfs(b_lvl[nxt])):
            visited[now] = True
            a_lvl[now] = nxt
            b_lvl[nxt] = now
            return True
    return False

n, m = map(int, input().split())
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
matching = 0
while True:
    bfs()
    flow = 0
    for i in range(MAX):
        if not visited[i] and dfs(i): flow += 1
    if flow == 0: break
    matching += flow
print(matching)
