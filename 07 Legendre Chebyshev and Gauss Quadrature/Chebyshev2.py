from GaussChebyshevQuadrature import quadChebyshev
from Evaluate import evalp

N = 6
points = 100
M = 10

polynomial = [[0 for x in range(N)] for x in range(N)] 

polynomial[0][0] = 1

for i in range(1, N):
    
    polynomial[i][i] = 1
    
    # Orthogonalization
    for j in range(i):
        
        f = lambda x: evalp(polynomial[i], x) * evalp(polynomial[j], x)
        
        integral1 = quadChebyshev(f, -1, 1, M)
        
        f = lambda x: evalp(polynomial[j], x) * evalp(polynomial[j] , x)
        
        integral2 = quadChebyshev(f, -1, 1, M)
        
        for k in range(j+1):
            
            polynomial[i][k] = polynomial[i][k] - integral1/integral2*polynomial[j][k]

for i in range(2, N):          
    # Normalization
    f = lambda x: evalp(polynomial[i], x) * evalp(polynomial[i], x)
    integral = quadChebyshev(f, -1, 1, M)
         
    for j in range(i+1):
        
        polynomial[i][j] = polynomial[i][j]/sqrt(integral)*sqrt(pi/2.0)

values = [[0 for x in range(100)] for x in range(N)]

for i in range(N):
    for j in range(points):
        values[i][j] = [(j-points/2.0)/(points/2.0), evalp(polynomial[i],  (j-points/2.0)/(points/2.0))]
        
for i in range(N):
    plot(values[i])