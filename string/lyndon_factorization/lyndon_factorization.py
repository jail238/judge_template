import sys
input = sys.stdin.readline

def duval(s):
    n = len(s)
    i, f = 0, []
    while i < n:
        j = i+1
        k = i
        while j<n and s[k]<=s[j]:
            if s[k]<s[j]: k = i
            else: k += 1
            j += 1
        step = j-k
        while i <= k:
            f.append(s[i:i+step])
            i += step
    return f

def min_cycle_string(s):
    s += s
    n = len(s)
    h, i, ans = n//2, 0, 0
    while i < h:
        ans = i
        j = i+1; k = i
        while j<n and s[k]<=s[j]:
            if s[k]<s[j]: k = i
            else: k += 1
            j += 1
        step = j-k
        while i<=k: i += step
    return ans
