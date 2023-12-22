import sys
input = sys.stdin.readline

def phi(x):
    def div2(x):
        ret = x
        while ~x & 1:
            x >>= 1
        if ret != x:
            ret >>= 1
        return ret, x
    ans, x = div2(x)
    p = 3
    while p*p <= x:
        if x%p == 0:
            ans -= ans//p
            while x % p == 0:
                x //= p
        p += 2
    
    if x > 1: return ans-(ans//x)
    return ans
