import matplotlib.mlab as mlab
import numpy.fft as npfft
from Tkinter import *
import matplotlib.pyplot as plt

def V(x):
    return 0.5 * (x-1.0)**2
    
def frame(psi, numberOfGridPoints, L, dt, ax1, ax2):
    for i in range(numberOfGridPoints):
        
        x = i*dx - L/2.0
        
        psi[i] = exp(-1j * V(x)*dt/2)*psi[i]
        
    # FFT
    psi2 = npfft.ifftshift(npfft.fft(npfft.fftshift(psi)))
    
    for i in range(numberOfGridPoints):
        
        k = i*2*pi/L - 2 * pi * numberOfGridPoints / (2 * L)
        
        psi2[i] = exp(-1j * 0.5*(k**2)*dt)*psi2[i]
        
    # iFFt
    psi = npfft.ifftshift(npfft.ifft(npfft.fftshift(psi2)))
    
    for i in range(numberOfGridPoints):
        
        x = i*dx - L/2.0
        
        psi[i] = exp(-1j * V(x)*dt/2)*psi[i]
    
    ax1.cla()
    ax1.plot([z.real for z in psi])
    ax1.plot([z.imag for z in psi])
    # Potential
    ax1.plot([V(j*dx - L/2.0) for j in range(numberOfGridPoints)])
    ax2.cla()
    ax2.plot([z.real for z in psi2])
    ax2.plot([z.imag for z in psi2])
    plt.ylim([-1,1])
    plt.gcf().canvas.draw()
    
    screen.after(16, frame, psi, numberOfGridPoints, L, dt, ax1, ax2)
    
screen = Tk()

f, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=True)

numberOfGridPoints = 2001
L = 30
psi = []
dx = L*1.0/(numberOfGridPoints-1)
dt = 0.01

# Gaussian distribution for initial condition
for i in range(numberOfGridPoints):
    psi += [sqrt(mlab.normpdf(i*dx - L/2.0, -4, 1))]
    
screen.after(1, frame, psi, numberOfGridPoints, L, dt, ax1, ax2)

#canv.update()

screen.mainloop()