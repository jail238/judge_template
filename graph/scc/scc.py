import sys
input = sys.stdin.readline

def scc(node):
    global ids, scc_cnt
    sstack = [(node, 0, -1)]
    while sstack:
        node, idx, ret = sstack.pop()
        if ids_arr[node] == 0 and ret == -1 and idx == 0:
            ids_arr[node], parents[node] = ids, ids
            ids += 1
            visited[node] = True
            stack.append(node)
        if ret != -1:
            child = graph[node][ret]
            parents[node] = min(parents[child], parents[node])
            idx = ret+1 
        while idx < len(graph[node]):
            now = graph[node][idx]
            if ids_arr[now] == 0:
                sstack.append((node, idx, idx))
                sstack.append((now, 0, -1))
                break
            elif visited[now]: parents[node] = min(parents[now], parents[node])
            idx += 1
        else:
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
