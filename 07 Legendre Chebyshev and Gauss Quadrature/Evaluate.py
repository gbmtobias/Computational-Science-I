def evalp(c, x) :
    n = len(c) - 1
    sum = c[-1]
    for k in range(n, 0,-1) :
        sum = x * sum + c[k - 1]
    return sum