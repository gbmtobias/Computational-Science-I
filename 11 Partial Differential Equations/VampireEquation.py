import matplotlib.pyplot as plt

def F(f, i, dx):
    return f[i] * (1 - f[i]) + (f[i+1]+f[i-1]-2*f[i])/(dx**2) 
    
numberOfGridPoints = 101
dx = 1.0/(numberOfGridPoints-1)
f = []
dt = 0.00001
numberOfTimeSteps = 2000

fig = plt.figure()
ax1 = fig.add_subplot(111)

# initial conditions
for i in range(numberOfGridPoints):
    if i > 40 and i < 60:
        f += [sin((i-40)*dx*5*pi)]
    else:
        f += [0]
    
# set boundaries to 0
f[0] = 0
f[-1] = 0

for i in range(numberOfTimeSteps):
    
    # set boundaries to 0
    fHalf = [0]
    
    for j in range(numberOfGridPoints-2):
        
        fHalf += [f[j+1] + 0.5*dt*F(f, j+1, dx)]
     
    # set boundaries to 0
    fHalf += [0]
    
    for j in range(numberOfGridPoints-2):
        
        f[j+1] = f[j+1] + dt*F(fHalf, j+1, dx)
    
    if i%400 == 0:
        x = np.arange(0., 1. + dx, dx)
        ax1.plot(x, f, label='t = ' + str(i*dt))
        
leg = ax1.legend(loc=1)

plt.show()