# A = 0, C = 1, G = 2, T = 3

def generateCodons():
    
    codons = []
    
    for i in range(4):
        for j in range(4):
            for k in range(4):
                codons += [[i , j, k]]
                
    return codons
    
def convertCodonsToDiamonds(codons):
    
    diamonds = []
    
    for i in range(len(codons)):
        diamonds += [[codons[i][0], codons[i][1], 3-codons[i][2], 3-codons[i][1]]]
        
    return diamonds
    
def getDifferentGamowDiamonds():
    
    differentDiamonds = []
    
    codons = generateCodons()
    
    diamonds = convertCodonsToDiamonds(codons)
    
    while len(diamonds) > 0:
        
        newDiamond = diamonds[0]
        del diamonds[0]
        
        differentDiamonds += [newDiamond]
        
        # remove equivalent diamonds
        n = 0
        while n < len(diamonds):
            
            equivalent = False
            
            if newDiamond == [diamonds[n][0], diamonds[n][3], diamonds[n][2], diamonds[n][1]]:
                equivalent = True
            elif newDiamond == [diamonds[n][2], diamonds[n][3], diamonds[n][0], diamonds[n][1]]:
                equivalent = True
            elif newDiamond == [diamonds[n][2], diamonds[n][1], diamonds[n][0], diamonds[n][3]]:
                equivalent = True
                    
            # remove equivalent diamonds        
            if equivalent:
                del diamonds[n]
            else:
                n += 1

    return differentDiamonds                