import numpy as np
from scipy import optimize
from math import cos, sin, pi

def err(params, xdata, ydata):
    
    projectedPoints = np.array([ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    
    for i in range(9):
        
        x = ydata[i*3+0] + params[0]
        y = ydata[i*3+1] + params[1]
        z = ydata[i*3+2] + params[2]
        
        projectedPoints[i*2+0] = x * params[3] / z
        projectedPoints[i*2+1] = y * params[3] / z
        
    return (projectedPoints - xdata)

picturePoints = np.array([294, 2269, 374, 2221, 438, 2182,
                        294, 2012, 375, 1980, 439, 1954,
                        294, 1755, 375, 1740, 440, 1727])
                        
gridPoints = np.array([-1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0,
                        0.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0,
                        0.0, -1.0, -1.0, 0.0, 0.0, -1.0, 0.0, 1.0, -1.0, 0.0])


angle = -71*pi/180     
                  
for i in range(9):
     
     x = cos(angle) * gridPoints[i*3+0] + sin(angle) * gridPoints[i*3+2]
     y = gridPoints[i*3+1]
     z = -sin(angle) * gridPoints[i*3+0] + cos(angle) * gridPoints[i*3+2]
     
     gridPoints[i*3+0] = x
     gridPoints[i*3+1] = y
     gridPoints[i*3+2] = z

                        
init = [100, 1, 100, 100]

p, success = optimize.leastsq(err, init, args=(picturePoints, gridPoints))