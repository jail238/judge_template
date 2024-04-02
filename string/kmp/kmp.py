#BOJ 1786

import sys
input = sys.stdin.readline

def pi_arr(p):
    pi = [0] * len(p)
    j = 0
    for i in range(1, len(p)):
        while j>0 and p[i] != p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    return pi

def kmp(pi, t):
    answer = []
    cnt = 0
    j = 0
    for i in range(len(t)):
        while j > 0 and t[i] != p[j]:
            j = pi[j-1]
        if t[i] == p[j]:
            if j == len(p)-1:
                answer.append(i-len(p)+2)
                cnt += 1
                j = pi[j]
            else: j += 1
    return cnt, answer

t = input().rstrip()
p = input().rstrip()
cnt, ans = kmp(pi_arr(p), t)
print(cnt)
for i in ans:
    print(i)
