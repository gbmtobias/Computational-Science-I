class Primenumber:
    def __init__(self, n):
    # generates the prime numbers between 1 and n
        self.primes = []
        self.nonPrimes = []
        
        for i in range(2, n+1):
            # check wether i is in the nonPrimes list
            prime = True
            for j in range(len(self.nonPrimes)):
                if self.nonPrimes[j] == i:
                    prime = False
            
            # if i is prime update lists
            if prime:
                self.primes.append(i)
                
                # add multiples of i to the nonPrimes list
                multiple = i * i
                factor = i
                while multiple <= n:
                    self.nonPrimes.append(multiple)
                    factor = factor + 1
                    multiple = factor * i