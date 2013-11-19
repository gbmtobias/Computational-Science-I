from scipy.integrate import odeint

omega = 1
    
def func(y, t):
    return [y[2]+y[1], y[3]-y[0], y[3]-y[0], -y[2]-y[1]+cos(omega*t)]
    
t = arange(0, 100, 0.1)

y0 = [0, 0, 0, 0]

y = odeint(func, y0, t)

plot(t, y)