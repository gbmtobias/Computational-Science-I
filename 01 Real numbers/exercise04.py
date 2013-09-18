import pylab

# encoded continued fractions series for mu
p = reduce(lambda s, n: s + [s[-1]*2], range(101), [2])

# invert the series
p = p[::-1]

# calculate mu from the series
mu = reduce(lambda s, n : n + 1/s, p, 1.)

# f defines the series of the partial sums
f = lambda s, n: s + [s[-1]+exp(pi*1j*n*n/mu)]

# calculate the series of the  partial sums
L = 10000
s = reduce(f,range(L+1),[0])

realList = [k.real for k in s] # list of all real parts
imgList = [k.imag for k in s] # list of all imaginary parts

pylab.plot(realList, imgList)

# remove last element of the list = first term of the continued fraction
p2 = p[0:-1]

# calculate mu2
mu2 = reduce(lambda s, n : n + 1/s, p2, 1.)

L2 = int(L/mu)
s2 = reduce(f,range(L2+1),[0])

realList2 = [k.real for k in s2] # list of all real parts
imgList2 = [k.imag for k in s2] # list of all imaginary parts

# add new figure for the 2nd plot
pylab.figure()

pylab.plot(realList2, imgList2)