# BOJ 10999

import sys
input = sys.stdin.readline

def bit_sum(tree, idx): # range 1~idx sum
    val = 0
    while idx > 0:
        val += tree[idx]
        idx -= (idx & -idx)
    return val

def bit_add(tree, idx, val): # init
    while idx <= n:
        tree[idx] += val
        idx += (idx & -idx)

def bit_range_update(l, r, val): # point/range_update
    bit_add(tree_a, l, val)
    bit_add(tree_a, r+1, -val)
    bit_add(tree_b, l, (-l+1)*val)
    bit_add(tree_b, r+1, r*val)

def bit_range_query(l, r): # point/range_value_output
    return bit_sum(tree_a, r)*r + bit_sum(tree_b, r) - bit_sum(tree_a, l-1)*(l-1) - bit_sum(tree_b, l-1)

n, m, k = map(int, input().split())
tree_a = [0 for _ in range(n+1)]
tree_b = [0 for _ in range(n+1)]
for i in range(1, n+1):
    v = int(input())
    bit_add(tree_b, i, v)

for i in range(m+k):
    a, *b = map(int, input().split())
    if a == 1:
        b, c, d = b[0], b[1], b[2]
        bit_range_update(b, c, d)
    else:
        b, c = b[0], b[1]
        print(bit_range_query(b, c))
