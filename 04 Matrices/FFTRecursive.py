from numpy import pi, arange, exp, concatenate
from pylab import subplot, plot, show
import sys

def testFFT():
    
    N = 64
    L = 8
    
    dx = 2.*L/N
    x = (arange(N) - N/2) * dx
    k = 2 * pi/(N * dx) * (arange(N) - N/2)
    f = 1/(1 + x*x)
    
    F = fft(f)
    
    F = concatenate((F[N/2:N], F[0:N/2]))
    
    subplot(212)
    plot(x, f)
    subplot(211)
    plot(k, F.real, color = "blue")
    plot(k, F.imag, color = "magenta")

    
def fft(f):
    
    N = len(f)
    
    if N%2 == 0:
        
        # split sum
        
        F_even = fft(f[::2])
        F_odd = fft(f[1::2])
        
        # get sums together
        
        w = exp(-2 * pi * 1j * arange(N)/N)
        
        F = concatenate(([F_even + w[:N/2] * F_odd,
                         F_even + w[N/2:] * F_odd]))
        
    else:
        
        if N > 1:
            print("Error: N must be a power of 2.")
            sys.exit(0)
        else:
            F = [f[0]]
            
    return F        