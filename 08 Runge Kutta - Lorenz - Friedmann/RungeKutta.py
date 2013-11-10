def rk4(f, y, h):
    
    k1 = f(y)
    k2 = f(y + 0.5*h*k1)
    k3 = f(y + 0.5*h*k2)
    k4 = f(y + h*k3)
    
    return y + 1/6.*h*(k1 + 2*k2 + 2*k3 + k4)
    
def rk1(f, y, h):
    
    k1 = f(y)
    
    return y + h*k1
    
def rk2(f, y, h):
    
    k1 = f(y)
    k2 = f(y + 0.5*h*k1)
    
    return y + h*k2