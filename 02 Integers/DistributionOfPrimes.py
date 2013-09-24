from Primenumber import Primenumber
import pylab

# get all primes between 1 and 100000
p = Primenumber(100000)

xAxis = p.primes

# calculate k*ln(p_k)
yAxis = reduce(lambda s, n: s + [n*log(p.primes[n-1])], range(1,len(p.primes)+1), [])

# plot p_k against k*ln(p_k)
pylab.xlabel("p_k")
pylab.ylabel("k*ln(p_k)")
pylab.plot(xAxis, yAxis)