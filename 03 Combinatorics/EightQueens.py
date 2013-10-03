from copy import copy

def searchSolutions(checkerboard = [-1, -1, -1, -1, -1, -1, -1, -1], n = 0, solutions = []):   
    
    for i in range(8):
        checkerboard[n] = i
        checkSolution(checkerboard, n, solutions)
        
    return solutions
    
def checkSolution(checkerboard, n, solutions):
    
    isValid = True
    
    for i in range(n):
        # check if queens are in the same row
        if checkerboard[n] == checkerboard[i]:
            isValid = False
        # check if queens are in the same diagonal
        if abs(checkerboard[n] - checkerboard[i]) == abs(n-i):
            isValid = False
    
    if isValid:
        if n == 7:
            # we have found a solution
            solutions += [copy(checkerboard)]
        else:
            # search in next column
            searchSolutions(checkerboard, n+1, solutions)
            
def convertSolutions(solutions):
    
    for i in range(len(solutions)):
        for j in range(8):
            solutions[i][j] = 2*j - 7 + (2*solutions[i][j] - 7)*1j        
            
def getIndependentSolutions():
    
    independentSolutions = []
    
    # search for all solutions
    solutions = searchSolutions()
    
    # convert the solutions to a complex representation
    convertSolutions(solutions)
    
    while len(solutions) > 0:
        newSolution = sorted(solutions[0], key=lambda x: x.real)
        del solutions[0]
        
        independentSolutions += [newSolution]
        
        # remove dependent solutions
        n = 0
        while n < len(solutions):
            dependent = False
            if newSolution == sorted([x * 1j for x in solutions[n]], key=lambda x: x.real):
                dependent = True
            elif newSolution == sorted([x * -1 for x in solutions[n]], key=lambda x: x.real):
                dependent = True
            elif newSolution == sorted([x * -1j for x in solutions[n]], key=lambda x: x.real):
                dependent = True
            elif newSolution == sorted([x.conjugate() for x in solutions[n]], key=lambda x: x.real):
                dependent = True
            elif newSolution == sorted([x.conjugate() * -1 for x in solutions[n]], key=lambda x: x.real):
                dependent = True
            elif newSolution == sorted([x.conjugate() * 1j for x in solutions[n]], key=lambda x: x.real):
                dependent = True
            elif newSolution == sorted([x.conjugate() * -1j for x in solutions[n]], key=lambda x: x.real):
                dependent = True
            
            if dependent:
                del solutions[n]
            else:
                n += 1
                
    return independentSolutions