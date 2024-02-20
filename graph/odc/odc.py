# BOJ 16911

import sys
input = sys.stdin.readline

def find(x):
    if p[x] == x: return x
    return find(p[x])

def union_rank(a, b):
    a, b = find(a), find(b)
    if a == b: return 0
    if rank[a] < rank[b]: a, b = b, a
    p[b] = a
    
    if rank[a] == rank[b]:
        rank[a] += 1
        stack.append((a, b, 1))
    else:
        stack.append((a, b, 0))
    return 1

def back(ct):
    for _ in range(ct):
        a = stack.pop()
        p[a[1]] = a[1]
        if a[2] == 1: rank[a[0]] -= 1

def divide(l, r, n):
    cnt = 0
    for i in segtree[n]:
        cnt += union_rank(find(i[0]), find(i[1]))
        
    if l == r:
        if find(query[l][0]) == find(query[l][1]): print(1)
        else: print(0)
        back(cnt)
        return
    
    m = (l+r)//2
    divide(l, m, n*2)
    divide(m+1, r, n*2+1)
    back(cnt)

def update(s, e, l, r, n, g1, g2):
    if r < s or e < l: return
    if l <= s and e <= r:
        segtree[n].append((g1, g2))
        return
    m = (s+e)//2
    update(s, m, l, r, n*2, g1, g2)
    update(m+1, e, l, r, n*2+1, g1, g2)

n, m = map(int, input().split())
stack = []
p = [i for i in range(200200)]
time = [[0, 0, 0, 0] for _ in range(200200)]
segtree = [[] for _ in range(800800)]
rank = [0 for _ in range(100100)]
edges = []
query = [[0, 0] for _ in range(200200)]
map_ = {}
c = 0

for i in range(1, m+1):
    x, a, b = map(int, input().split())
    if a > b: a, b = b, a
    if x == 1:
        map_[(a, b)] = i
        time[i][0], time[i][1], time[i][2], time[i][3] = a, b, c+1, -1
    
    elif x == 2:
        j = map_[(a, b)]
        time[j][3] = c
        edges.append((time[j][0], time[j][1], time[j][2], time[j][3]))
    
    elif x == 3:
        c += 1
        query[c][0], query[c][1] = a, b

for i in range(1, m+1):
    if time[i][3] == -1:
        time[i][3] = c
        edges.append((time[i][0], time[i][1], time[i][2], time[i][3]))

for edge in edges:
    update(1, c, edge[2], edge[3], 1, edge[0], edge[1])

divide(1, c, 1)
