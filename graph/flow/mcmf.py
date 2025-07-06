from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e12)

class MCMF:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n+1)]
        self.inf = INF
        self.dist, self.visited, self.node, self.edge = [], [], [], []

    def add_edge(self, u, v, capacity, cost):
        self.adj[u].append([v, capacity, cost, len(self.adj[v])])
        self.adj[v].append([u, 0, -cost, len(self.adj[u])-1])

    def spfa(self, s, t):
        self.dist = [self.inf for _ in range((self.n+1))]
        self.visited = [0 for _ in range((self.n+1))]
        self.node = [-1 for _ in range((self.n+1))]
        self.edge = [-1 for _ in range((self.n+1))]
        q = deque([s])
        self.dist[s] = 0
        self.visited[s] = True

        while q:
            u = q.popleft()
            self.visited[u] = False
            for i, (v, cap, cost, _) in enumerate(self.adj[u]):
                if cap > 0 and self.dist[v]>self.dist[u]+cost:
                    self.dist[v] = self.dist[u]+cost
                    self.node[v] = u
                    self.edge[v] = i
                    if not self.visited[v]:
                        q.append(v)
                        self.visited[v] = 1
        return self.dist[t] != self.inf

    def solve(self, s, t, maxf=INF):
        max_flow, min_cost = 0, 0
        while max_flow < maxf and self.spfa(s, t):
            flow = self.inf
            now = t
            while now != s:
                prev = self.node[now]
                edge_idx = self.edge[now]
                flow = min(flow, self.adj[prev][edge_idx][1])
                now = prev
            flow = min(flow, maxf-max_flow)
            max_flow += flow
            min_cost += flow*self.dist[t]
            now = t
            while now != s:
                prev = self.node[now]
                edge_idx = self.edge[now]
                self.adj[prev][edge_idx][1] -= flow
                rev_edge_idx = self.adj[prev][edge_idx][3]
                self.adj[now][rev_edge_idx][1] += flow
                now = prev
        return max_flow, min_cost

mcmf = MCMF(111)
