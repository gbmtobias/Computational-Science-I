from Primenumber import Primenumber

def getCarmichaelNumbers(N) :
# calculates all carmichael numbers between 1 and N
    
    carmichaelNumbers = []
    
    p = Primenumber(N)    
    
    for i in range(1, N+1) :
        
        canBeCarmichael = True
        
        # check all numbers j coprime to i wether they fullfil
        # the equation pow(j, i - 1, i) == 1
        for j in range(i) :
            if gcd(i, j) == 1 :
                if pow(j, i - 1, i) != 1 :
                    # can't be a carmichael number
                    canBeCarmichael = False
                    break
        
        # if i is a candidate for a carmichael number,
        # check if it's prime
        if canBeCarmichael :
            if i not in p.primes :
                carmichaelNumbers = carmichaelNumbers + [i]
    
    return carmichaelNumbers
              
def printCarmichaelNumbers(N) :
# prints all carmichael numbers between 1 and N
    c = getCarmichaelNumbers(N)
    
    for i in range(len(c)) :
        print(c[i])
        
def gcd(a, b) :
# returns the greates common divisor
    if b == 0 :
        return a
    r = a%b
    return gcd(b, r)