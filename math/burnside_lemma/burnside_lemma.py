from math import gcd
import sys
input = sys.stdin.readline

def burnside_lemma(n, m):
    ans = 0
    for i in range(n):
        ans += pow(m, gcd(i, n))
    if n%2 == 0: ans += (pow(m, n//2)+pow(m, n//2+1))*(n//2) # 좌우대칭도 확인할 때 사용
    else: ans += pow(m, (n+1)//2)*n
    return ans//(2*n)

c, s = map(int, input().split())
print(burnside_lemma(c, s))
