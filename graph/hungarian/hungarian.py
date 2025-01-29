import sys
input = sys.stdin.readline
INF = int(1e6)

class Hungarian:
    def __init__(self, n):
        self.n = n
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    def add_matrix(self, mat): self.matrix = mat

    def hungarian(self):
        u, v, matching = [0 for _ in range(self.n+1)], [0 for _ in range(self.n+1)], [0 for _ in range(self.n+1)]
        agu_path = [0 for _ in range(self.n+1)]
        for i in range(1, self.n+1):
            matching[0] = i
            cur_min = [INF for _ in range(self.n+1)]
            used = [False for _ in range(self.n+1)]
            now = 0
            while True:
                used[now] = True
                mat_now = matching[now]
                delta = INF
                nxt = 0
                for j in range(1, self.n+1):
                    if not used[j]:
                        cur = self.matrix[mat_now-1][j-1]-u[mat_now]-v[j]
                        if cur < cur_min[j]:
                            cur_min[j] = cur
                            agu_path[j] = now
                        if cur_min[j] < delta:
                            delta = cur_min[j]
                            nxt = j
                for j in range(self.n+1):
                    if used[j]:
                        u[matching[j]] += delta
                        v[j] -= delta
                    else:
                        cur_min[j] -= delta
                now = nxt
                if matching[now] == 0: break
            while True:
                nxt = agu_path[now]
                matching[now] = matching[nxt]
                now = nxt
                if now == 0: break
        return -v[0]

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
hungarian = Hungarian(n)
hungarian.add_matrix(matrix)
print(hungarian.hungarian())
