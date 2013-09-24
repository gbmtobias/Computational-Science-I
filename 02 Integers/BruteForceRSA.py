def decrypt(b, c, N) :
    i = 1
    while i <= N :
        if pow(b, i, N) == 1 :
            r = i
            break
        i += 1
    
    i = 1
    while i <= N :
        if (c*i)%r == 1 :
            d = i
            break
        i += 1
    
    return word(pow(b, d, N))

def word(n) :
    str = ""
    while n > 0 :
        c = chr(n % 32 + 96)
        if c < "a" or c > "z" :
            c = " "
        str += c
        n /= 32
    return str