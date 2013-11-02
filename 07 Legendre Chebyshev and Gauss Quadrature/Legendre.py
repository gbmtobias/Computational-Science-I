from FivePoint import fivepoint
from Evaluate import evalp

N = 6
points = 100
B = 50

polynomial = [[0 for x in range(N)] for x in range(N)] 

polynomial[0][0] = 1

for i in range(1, N):
    
    polynomial[i][i] = 1
    
    # Orthogonalization
    for j in range(i):
        
        f = lambda x: evalp(polynomial[i], x) * evalp(polynomial[j], x)
        
        integral1 = fivepoint(f, -1, 1, B)
        
        f = lambda x: evalp(polynomial[j], x) * evalp(polynomial[j], x)
        
        integral2 = fivepoint(f, -1, 1, B)
        
        for k in range(j+1):
            
            polynomial[i][k] = polynomial[i][k] - integral1/integral2*polynomial[j][k]

for i in range(2, N):          
    # Normalization
    f = lambda x: evalp(polynomial[i], x) * evalp(polynomial[i], x)
    integral = fivepoint(f, -1, 1, B)
         
    for j in range(i+1):
        
        polynomial[i][j] = polynomial[i][j]/sqrt(integral)*1.0/sqrt(i+0.5)

values = [[0 for x in range(100)] for x in range(N)]

for i in range(N):
    for j in range(points):
        values[i][j] = [(j-points/2.0)/(points/2.0), evalp(polynomial[i],  (j-points/2.0)/(points/2.0))]
        
for i in range(N):
    plot(values[i])