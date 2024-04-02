import sys
input = sys.stdin.readline

def init(n):
    for i in range(n):
        tree[i+n] = arr[i]
    for i in range(n-1, 0, -1):
        tree[i] = tree[i<<1] + tree[i<<1|1]

def query(tree, l, r, n):
    l += n
    r += n
    t = 0
    while l < r:
        if l&1:
            t += tree[l]
            l += 1
        if r&1:
            r -= 1
            t += tree[r]
        l >>= 1
        r >>= 1
    return t

def update(tree, idx, n):
    idx += n
    tree[idx] = 1
    while idx > 1:
        tree[idx>>1] = tree[idx]+tree[idx^1]
        idx = idx>>1

n = int(input())
tree = [0 for _ in range(n*2+100)]
arr = list(map(int, input().split()))
