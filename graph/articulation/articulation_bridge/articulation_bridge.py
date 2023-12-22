# BOJ 11400
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
INF = int(1e6)

def dfs(now, p):
    global cnt
    cnt += 1
    visited_n[now] = cnt
    visited[now] = True
    temp_n = visited_n[now]
    for nxt in graph[now]:
        if nxt == p:
            continue
        if visited[nxt]:
            temp_n = min(temp_n, visited_n[nxt])
            continue
        visited[nxt] = True
        pre_n = dfs(nxt, now)
        if pre_n > visited_n[now]: ans.append((min(now, nxt), max(now, nxt)))
        temp_n = min(temp_n, pre_n)
    return temp_n

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
visited = [False for _ in range(v+1)]
visited_n = [INF for _ in range(v+1)]
ans = []
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
for i in range(1, v+1):
    if not visited[i]: dfs(i, 0)
print(len(ans))
for i in sorted(ans):
    print(*i)
