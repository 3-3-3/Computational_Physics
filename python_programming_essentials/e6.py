def s(n):
    return sum([((-1)**k*k)/2**k for k in range(1, n+1)])
