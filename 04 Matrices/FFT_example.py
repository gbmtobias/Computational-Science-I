from numpy import pi, arange, concatenate
from scipy import fft
from pylab import subplot, plot, show

N = pow(2, 6)
L = 8
dx = 2. * L/N
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