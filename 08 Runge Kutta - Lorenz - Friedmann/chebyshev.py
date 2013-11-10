from RungeKutta import rk4, rk2, rk1
import numpy

f = lambda u1, u2, u3, n: numpy.array([u2, (u3*u2-n**2*u1)/(1-u3**2), 1])

rk = (rk1, rk2, rk4)

for k in range(3):
    
    figure()

    for i in range(6):
        
        g = lambda (x, y, z): f(x, y, z, i)
        
        # evaluate g on [0, 1]
        h = 0.01    
        T = 0
        y = [numpy.array([cos(i*pi/2), i*sin(i*pi/2), 0])]
        x1 = [0]
        fx1 = [cos(i*pi/2)]
        
        while T < 1:
            y += [rk[k](g, y[-1], h)]
            fx1 += [y[-1][0]]
            T += h
            x1 += [T]
        
        # evaluate g on [0, -1]    
        T = 0
        y = [numpy.array([cos(i*pi/2), i*sin(i*pi/2), 0])]
        x2 = [0]
        fx2 = [cos(i*pi/2)]
        
        while T > -1:
            y += [rk[k](g, y[-1], -h)]
            fx2 += [y[-1][0]]
            T -= h
            x2 += [T]
        
        plot(x2[::-1]+x1, fx2[::-1]+fx1)