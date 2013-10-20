import pylab
import random

def walkRandom(N):
    
    x = 0
    y = 0
    distance = 0
    
    for i in range(N):
        xSteps = random.random() - 0.5
        ySteps = random.random() - 0.5
        
        distance = sqrt(xSteps*xSteps + ySteps*ySteps)
        
        x += xSteps/distance
        y += ySteps/distance
        
    traveledDistance = sqrt(x*x + y*y)
        
    return (traveledDistance, x, y)
    
def simulateRandomWalks():
    
    distance = []
    xValues = []
    yValues = []
    
    for i in range(10000):
        
        distance += [walkRandom(50)[0]]
        xValues += [walkRandom(50)[1]]
        yValues += [walkRandom(50)[2]]
    
    subplot(311)
    hist(distance, bins=100, normed=True, histtype='step')    
    subplot(312)
    hist(xValues, bins=100, normed=True, histtype='step')
    subplot(313)
    hist(yValues, bins=100, normed=True, histtype='step')