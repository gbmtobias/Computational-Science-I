def fivepoint( f , a, b, B = 1) :
# Compute integral of f between a and b
# using B blocks of the 5-point integrator.

    integral = 0

    blockLength = (b - a)/(B*1.)
    
    for i in range(B):
        
        c = a + i * blockLength
        d = a + (i+1) * blockLength
        
        integral += (d-c)/10.*(1375./576. * f((d-c)/10.*-4. + (c+d)/2.) + 125/144. * f((d-c)/10.*-2. + (c+d)/2.) + 335/96. * f((c+d)/2) + 125./144. * f((d-c)/10.*2. + (c+d)/2.) + 1375./576. * f((d-c)/10.*4. + (c+d)/2.))
        
    return integral