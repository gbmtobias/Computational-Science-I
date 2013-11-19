from scipy.integrate import odeint

omega = -2
epsilon = 0.3
    
def func(y, t):
    return [-sin(y[1])-epsilon*sin(y[1]-omega*t), y[0]]
    
t = arange(0, 1000, 0.1*2*pi/-omega)

for n in range(100) :

    pini = 0.01*n
    
    y0 = [pini, 0]
    
    y = odeint(func, y0, t)
    
    for i in range(100):
        plot(y[i*10][0], y[i*10][1], 'r,')