from math import log2, ceil
import sys
input = sys.stdin.readline

def init(node, l, r):
    if l == r: tree[node] = arr[l]
    else:
        m = (l+r)//2
        init(node*2, l, m); init(node*2+1, m+1, r)
        tree[node] = tree[node*2]+tree[node*2+1]

def lazy_pp(node, s, e):
    if lazy[node] != 0:
        tree[node] += (e-s+1)*lazy[node]
        if s != e:
            lazy[node*2] += lazy[node]; lazy[node*2+1] += lazy[node]
        lazy[node] = 0

def update(node, s, e, l, r, val):
    lazy_pp(node, s, e)
    if l > e or r < s: return
    if l <= s and e <= r:
        tree[node] += (e-s+1)*val
        if s != e:
            lazy[node*2] += val
            lazy[node*2+1] += val
        return
    m = (s+e)//2
    update(node*2, s, m, l, r, val); update(node*2+1, m+1, e, l, r, val)
    tree[node] = tree[node*2] + tree[node*2+1]

def query(node, s, e, l, r):
    lazy_pp(node, s, e)
    if l > e or r < s: return 0
    if l <= s and e <= r: return tree[node]
    m = (s+e)//2
    return query(node*2, s, m, l, r)+query(node*2+1, m+1, e, l, r)

n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
h = ceil(log2(n))
tree = [0 for _ in range(2**(h+1))]
lazy = [0 for _ in range(2**(h+1))]
init(1, 0, n-1)

for _ in range(m+k):
    a, *b = map(int, input().split())
    if a == 1:
        b, c, d = b[0]-1, b[1]-1, b[2]
        update(1, 0, n-1, b, c, d)
    else:
        b, c = b[0]-1, b[1]-1
        print(query(1, 0, n-1, b, c))
