from Primenumber import Primenumber

def getZetaAsSum(z):
# gets the value of the riemann zeta function for z

    # returns the first 1000 summands
    return reduce(lambda s, n: s + pow(n, -z), range(1,1001), 0)
    
def getZetaAsProduct(z):
# gets the value of the riemann zeta function for z
    
    # the first 1000 primes are smaller than 8000
    p = Primenumber(8000)
    
    # returns the first 1000 factors
    return reduce(lambda s, n: s * 1/(1 - pow(p.primes[n], -z)), range(1000), 1)