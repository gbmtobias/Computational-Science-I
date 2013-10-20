import pylab
import random

def run():
    
    D = 30
    M = 40
    
    maxFractDifferences = []
    
    for i in range(100000):
        
        currentD = D
        currentM = M
    
        maxFractDiff = 1.0*abs(currentD - currentM)/(D + M)
        
        while currentD > 0 and currentM > 0:
        
            # Choose randomly from D or M            
            
            randomChoice = random.random()
            
            if randomChoice < 0.5:
                currentD -= 1
            else:
                currentM -= 1 
                
            if 1.0*abs(currentD - currentM)/(D + M) > maxFractDiff:
                maxFractDiff = 1.0*abs(currentD - currentM)/(D + M)
                
        maxFractDifferences += [maxFractDiff]
        
    # Print statistics from simulation
    hist(maxFractDifferences, bins=20, histtype='step', normed=True, cumulative=True)    
        
    # Print KS statistics
    
    v = sqrt(D*M/(D+M))
    
    mu = v + 0.12 + 0.11/v
    
    s = arange(0.01, 1, 0.01)
    
    pksInv = [1 - 2 * reduce(lambda res, k : res + (-1)**k * exp(-2 *
        (k+1)**2 * mu**2 * t**2), range(100), 0) for t in s]
        
    pylab.plot(s, pksInv)