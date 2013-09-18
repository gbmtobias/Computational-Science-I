class Fraction :
    def __init__(self, a, b):
    # sets the value for a fraction of the form a/b
        c = gcd(a, b)
        self.numerator = a/c
        self.denominator = b/c
        
def gcd(a, b) :
# returns the greatest common divisor of a and b
    if b == 0 :
        return a
    r = a%b
    return gcd(b, r)
    
def lcm(a, b) :
# returns the least common divisor of a and b
    return abs(a*b)/gcd(a,b)
    
def pi(accuracy = 1000) :
    series = []
    
    n = 1
    sign = 1
    # calculate all summands
    while n < 2*accuracy :
        series = series + [Fraction(sign*16,n*pow(5,n))]
        series = series + [Fraction(-sign*4,n*pow(239,n))]
        n = n + 2
        sign = sign * -1
        
    # get least common multiple of all denominators
    lcmDenominator = series[0].denominator
    for i in range(len(series)-1) :
        lcmDenominator = lcm(lcmDenominator, series[i+1].denominator)
    
    # calculate numerator
    numerator = 0
    for i in range(len(series)) :
        numerator = numerator + series[i].numerator*lcmDenominator/series[i].denominator
    
    result = ""    
    
    result = result + str(numerator/lcmDenominator) + "."
    
    numerator = numerator%lcmDenominator
    
    decimal = 1
    while decimal < accuracy :
        digit = (numerator*10)/lcmDenominator
        numerator = (numerator*10)%lcmDenominator
        result = result + str(digit)
        decimal = decimal + 1
    
    return result