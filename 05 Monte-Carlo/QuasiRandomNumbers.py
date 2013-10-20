import pylab
import random

def getHaltonNumber(n, base):
    
    halton = 0
    exponent = 0
    
    while n > 0:
        r = n%base
        n = n/base
        
        exponent -= 1
        halton += r * pow(base, exponent)
        
    return halton
        
def testSequences():
    
    # plot Halton sequence
    
    for i in range(512):
        pylab.plot(getHaltonNumber(i+1, 3), getHaltonNumber(i+1, 5), 'bo')
            
    pylab.figure()
    
    for i in range(512):
        pylab.plot(random.random(), random.random(), 'bo')