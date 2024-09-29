import sys
input = sys.stdin.readline

n = int(input())
div, i, k = {}, 2, n
while i*i <= k:
    while k%i == 0:
        if not i in div: div[i] = 1
        else: div[i] += 1
        k //= i
    i += 1
if k != 1:
    if not k in div: div[k] = 1
    else: div[k] += 1