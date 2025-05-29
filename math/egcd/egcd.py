def egcd(a, b):
    x, y, s, t = 0, 1, 1, 0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-s*q, y-t*q
        a, b, x, y, s, t = r, a, s, t, m, n
    return b, x, y #gcd, x0, y0

# ax+by+c = 0이 주어졌을 때 gcd(a, b)와 x0, y0의 실제 값
a, b, c = map(int, input().split())
g, x0, y0 = egcd(a, b)
if -c%g != 0: print(-1); exit() #해가 없음
tmp = -c//g
x0, y0 = x0*tmp, y0*tmp
