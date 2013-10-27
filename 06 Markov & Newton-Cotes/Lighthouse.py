import random
import pylab

def run():
    a = -0.5
    b = 0.7
    
    x = []
    
    for i in range(500):
        phi = random.random() * 2 * pi
        value = a + b * tan(phi)
        
        if value >= -1 and value <= 1:
            x += [value]
            
    u = [random.random()*2 - 1]
    v = [random.random()]
            
    for i in range(1000):
        u += [random.random()*2 - 1]
        v += [random.random()]
        r = random.random()
        
        jointDensity1 = reduce(lambda s, n: s + log(p(x[n], u[-1], v[-1])), range(len(x)), 0)
        jointDensity2 = reduce(lambda s, n: s + log(p(x[n], u[-2], v[-2])), range(len(x)), 0) 
        
        if exp(jointDensity1 - jointDensity2) <= r:
            u[-1] = u[-2]
            v[-1] = v[-2]
    
    subplot(311)
    hist(x, bins=40, histtype='step', normed=True)
    subplot(312)        
    hist(u, bins=40, histtype='step', normed=True)
    subplot(313)
    hist(v, bins=40, histtype='step', normed=True)
            
def p(x, a, b):
    
    return (1/(1 + ((x-a)/b)**2)*1/b) / (arctan((1-a)/b) - arctan((-1-a)/b))