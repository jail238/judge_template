import sys
input = sys.stdin.readline

def is_QR(n, p):
    n%=p
    if n == 0: return True
    return pow(n, (p-1)//2, p) == 1

def base_convert(n, b):
    if n < 2: return [n]
    ans = []
    while n != 0:
        ans.append(n%b)
        n //= b
    return ans[::-1]

def cipolla_mult(t1, t2, w, p):
    a, b = t1
    c, d = t2
    return ((a*c+b*d*w)%p, (a*d+b*c)%p)

def cipolla(n, p):
    n %= p
    if n <= 1: return (n, -n%p)
    phi = p-1
    if not is_QR(n, p): return ()
    if p%4 == 3:
        ans = pow(n, (p+1)//4, p)
        return (ans, -ans%p)
    aa = 0
    for i in range(1, p):
        tmp = pow((i*i-n)%p, phi//2, p)
        if tmp == phi: aa = i; break
    exponent = base_convert((p+1)//2, 2)
    x1 = (aa, 1)
    x2 = cipolla_mult(x1, x1, aa*aa-n, p)
    for i in range(1, len(exponent)):
        if exponent[i] == 0:
            x2 = cipolla_mult(x2, x1, aa*aa-n, p)
            x1 = cipolla_mult(x1, x1, aa*aa-n, p)
        else:
            x1 = cipolla_mult(x1, x2, aa*aa-n, p)
            x2 = cipolla_mult(x2, x2, aa*aa-n, p)
    return (x1[0], -x1[0]%p)

n, p = map(int, input().split())
print(cipolla(n, p))
