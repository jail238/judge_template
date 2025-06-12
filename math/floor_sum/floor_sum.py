# sum(i=0..n)_(floor((ai+b)/c)) => O(logn)

def floor_sum(a, b, c, n):
    ans, sign = 0, 1
    while n >= 0:
        if a == 0: ans += sign*(n+1)*(b//c); break
        if a >= c or b >= c:
            t1, t2 = (n*(n+1)//2)*(a//c), (n+1)*(b//c)
            ans += sign*(t1+t2)
            a %= c; b %= c
        else:
            m = (a*n+b)//c
            if m == 0: break
            ans += sign*n*m
            b, n = c-b-1, m-1
            a, c = c, a
            sign *= -1
    return ans
