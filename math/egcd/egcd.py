def egcd(a, b):
    x, y, s, t = 0, 1, 1, 0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-s*q, y-t*q
        a, b, x, y, s, t = r, a, s, t, m, n
    return b, x, y #gcd, x0, y0
