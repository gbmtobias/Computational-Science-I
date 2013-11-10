H0 = 1
Omega_m = 1
Omega_l = 1

def H(a):
    return H0*sqrt(Omega_m/(a**3)+Omega_l)
    
def func(y, t):
    return [-1./(t*H(t)), -1./(t**2*H(t))]
    
t = arange(1, 0.3, -0.01)
y0 = [0, 0]

y = odeint(func, y0, t)

plot(t, y)