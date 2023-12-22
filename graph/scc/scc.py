import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def scc(node):
    global ids, scc_cnt
    ids_arr[node], parents[node] = ids, ids
    ids += 1; visited[node] = True
    stack.append(node)
    
    for now in graph[node]:
        if ids_arr[now] == 0:
            scc(now)
            parents[node] = min(parents[now], parents[node])
        elif visited[now]:
            parents[node] = min(parents[now], parents[node])
    
    w = -1
    if parents[node] == ids_arr[node]:
        while w != node:
            w = stack.pop()
            scc_idx[w] = scc_cnt
            visited[w] = False
        scc_cnt += 1

v, e = map(int, input().split())
graph = [[] for _ in range((v+1))]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
stack = []
visited = [False]*(v+1)
ids, ids_arr = 1, [0]*(v+1)
parents, scc_idx, scc_cnt = [0]*(v+1), [-1]*(v+1), 0

for i in range(1, v+1):
    if ids_arr[i] == 0: scc(i)

indegree = [0 for _ in range(scc_cnt)]
for i in range(1, v+1):
    for j in graph[i]:
        if scc_idx[i] != scc_idx[j]:
            indegree[scc_idx[j]] += 1
