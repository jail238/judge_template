# σ(n) is sum of divisors of n (n의 양의 약수의 합)
# sum_sigma(n) is σ(1)+σ(2)+...+σ(n) (O(sqrt(N)))
def sum_sigma(n):
    s, e, res = 1, 0, 0
    while s <= n:
        e = (n//(n//s))
        res += (s+e)*(e-s+1)//2*(n//s)
        s = e+1
    return res
