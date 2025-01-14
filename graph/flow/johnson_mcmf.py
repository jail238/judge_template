from heapq import *
from collections import deque
import sys
input = sys.stdin.readline

class MCMF:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.potential = [0 for _ in range(n)]

    def add_edge(self, u, v, capacity, cost):
        self.adj[u].append([v, capacity, cost, len(self.adj[v])])
        self.adj[v].append([u, 0, -cost, len(self.adj[u])-1])

    def spfa(self, source):
        INF = int(1e9)
        dist = [INF for _ in range(self.n)] 
        visited = [False for _ in range(self.n)]
        dist[source] = 0
        q = deque([source])
        visited[source] = True
        while q:
            u = q.popleft()
            visited[u] = False
            for v, capacity, cost, _ in self.adj[u]:
                if capacity > 0 and dist[v] > dist[u] + cost:
                    dist[v] = dist[u] + cost
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
        for i in range(self.n):
            if dist[i] < INF: self.potential[i] = dist[i]

    def dijkstra_potential(self, source):
        INF = int(1e9)
        dist = [INF for _ in range(self.n)]
        dist[source] = 0
        parent = [(-1, -1) for _ in range(self.n)] 
        heap = []
        heappush(heap, (0, source))

        while heap:
            cur, u = heappop(heap)
            if dist[u] < cur: continue
            for i in range(len(self.adj[u])):
                v, capacity, cost = self.adj[u][i][0], self.adj[u][i][1], self.adj[u][i][2]
                if capacity > 0:
                    nxt = cur+cost+self.potential[u]-self.potential[v]
                    if dist[v] > nxt:
                        dist[v] = nxt
                        parent[v] = (u, i)
                        heappush(heap, (nxt, v))
        return dist, parent

    def mcmf(self, source, sink):
        self.spfa(source)
        INF, flow, cost = int(1e9), 0, 0
        while True:
            dist, parent = self.dijkstra_potential(source)
            if dist[sink] == INF: break
            for i in range(self.n):
                if dist[i] < INF: self.potential[i] += dist[i]
            incre_flow, v = INF, sink
            while v != source:
                u, edge_idx = parent[v]
                if u == -1: incre_flow = 0; break
                cap = self.adj[u][edge_idx][1]
                incre_flow = min(incre_flow, cap)
                v = u
            if incre_flow == 0 or incre_flow == INF: break
            v, tmp = sink, 0
            while v != source:
                u, edge_idx = parent[v]
                cost_uv = self.adj[u][edge_idx][2]
                rev = self.adj[u][edge_idx][3]
                self.adj[u][edge_idx][1] -= incre_flow
                self.adj[v][rev][1] += incre_flow
                tmp += cost_uv
                v = u
            flow += incre_flow
            cost += incre_flow*tmp
        return flow, cost

n = int(input())
INF, SIZE = int(1e9), 555
mcmf = MCMF(SIZE)
# mcmf.add_edge(a, b, capacity, cost)
src, sink = 2*n+1, 2*n+2
flow, cost = mcmf.mcmf(src, sink)
print(flow, cost)
