eps = 1.0
exponent = 0

while 1 + eps > 1 :
    # decrease eps as long as 1+eps>1
    exponent = exponent + 1
    eps = pow(2.0, -exponent)
    
mbits = exponent-1 # bits of the mantissa
    
print("The mantissa has %d bits + 1 bit for the sign" % mbits)

exponent = 0

while True :
    # increase exponent as long as no overflow occurs
    exponent = exponent + 1
    try:
        delta = pow(2.0, exponent)
    except (ArithmeticError):
        break

maxExponent = exponent - 1 # gratest possible exponent

exponent = 0

eps = pow(2.0, -mbits)

while delta + eps*delta > delta :
    # decrease exponent as long as there is no loss of precision
    exponent = exponent - 1
    delta = pow(2.0, exponent)

minExponent = exponent + 1 # smallest posssible exponent
    
ebits = log((maxExponent+1)-(minExponent-1)+1)/log(2) # bits of the exponent
    
print("The exponent has %d bits" % ebits)