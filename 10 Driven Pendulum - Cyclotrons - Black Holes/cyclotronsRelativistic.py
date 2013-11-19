from scipy.integrate import odeint

omega = 1
alpha = 1
    
def func(y, t):
    a = sqrt(1+(y[2]+y[1])**2+(y[3]-y[0])**2)
    return [(y[2]+y[1])/a, (y[3]-y[0])/a, (y[3]-y[0])/a, -(y[2]+y[1])/a+alpha*cos(omega*t)]
    
t = arange(0, 100, 0.1)

y0 = [0, 0, 0, 0]

y = odeint(func, y0, t)

plot(t, y)