from scipy.integrate import odeint

alpha = 3
    
def func(y, t):
    return [alpha * y[0] - y[0]*y[1], y[0]*y[1] - y[1]]
    
t = arange(0, 20, 0.01)
y0 = [2, 1]

y = odeint(func, y0, t)

plot(t, y)