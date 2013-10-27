from scipy.linalg import solve

def getCoefficients():

    A = [[1./2, 1, 1],[0, 2**2, 4**2],[0, 2**4, 4**4]]
         
    B = [[5], [1./3*(5**3)], [1./5*(5**5)]]
    
    X = solve(matrix(A), matrix(B))
    
    for i in range(3):
        
        coeff = []
        
        while X[i] < pow(10,8):
        
            coeff += [floor(X[i])]
            X[i] = 1./(X[i]-floor(X[i]))
            
        numerator = coeff[-1]
        denominator = 1
            
        for j in range(len(coeff)-1):
    
            temp = denominator
            denominator = numerator
            numerator = temp
            numerator = numerator + coeff[-(j+2)]*denominator
            
        c = gcd(numerator[0], denominator[0])
            
        print numerator[0]/c, "/", denominator[0]/c
    
def gcd(a, b):
# returns the greatest common divisor of a and b
    if b == 0 :
        return a
    r = a%b
    return gcd(b, r)