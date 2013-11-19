omega = -2
epsilon = 0.3
    
dt = 0.1*2*pi/-omega

for n in range(100) :

    pini = 0.01*n
    
    p = [pini, 0]
    
    q = [0, 0]
    
    s = [0, 0]
    
    for i in range(200):
        
        q = [q[0] + p[0]*dt/2, q[1] + omega*dt/2]
        s = [sin(q[0]), epsilon*sin(q[0]-q[1])]
        p = [p[0] - (s[0]+s[1])*dt, p[1]+s[1]*dt]
        q = [q[0] + p[0]*dt/2, q[1] + omega*dt/2]
    
        if i%10==0:
            plot(p[0], q[0], 'r,')
