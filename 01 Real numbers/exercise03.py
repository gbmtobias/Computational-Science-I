def power(x, n) :
# returns x^n for x and an integer n
    if type(n) != type(0):
        raise TypeError("n must be an integer")
    
    if n == 1 :
        return x
        
    if n == 0 :
        return 1
     
    if n%2 == 0 :
        y = power(x, n/2) * power(x, n/2)
    else :
        y = x * power(x, n-1)
        
    return y
    

def nroot(x, n = 2) :
# returns n-th root of x > 0 and an integer n
    
    if x <=0 :
        raise ArithmeticError("The n-th root is only defined for positive numbers")
        
    if type(n) != type(0):
        raise TypeError("n must be an integer")
        
    eps = sys.float_info.epsilon

    root = x
    
    delta = float((power(root, n) - x))/(n*power(root, n-1))
    
    while  abs(delta) > root*eps : # check if underflow happens
        # Newton-Raphson method
        root = root - delta
        delta = float((power(root, n) - x))/(n*power(root, n-1))
        
    return root