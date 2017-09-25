def fac(n):
    if n > 1:
        return n * fac(n-1)
    elif n >= 0:
        return 1

def com_fac(n, r):
    if n >= r:
        return fac(n) // (fac(r) * fac(n-r))

def com_rec(n, r):
    if r == 0:
        return 1
    elif n < r:
        return 0
    else:
        return com_rec(n-1, r-1) + com_rec(n-1, r)


