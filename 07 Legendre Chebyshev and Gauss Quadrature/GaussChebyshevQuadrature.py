from math import *

def quadChebyshev( f , a, b, M = 5) :
# Compute integral of f between a and b
# using B blocks of the M-point integrator.

    integral = 0

        
    for j in range(M):
        
        integral += (b-a)/2.*pi/M*f((b-a)/2. * cos((j+0.5)*pi/M) + (a+b)/2.)
        
    return integral