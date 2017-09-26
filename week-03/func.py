
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
def timesFive(a):
    return a * 5

def absolute(a):
    return abs(a)

def oneUp(a):
    return a + 1

def squirred(a):
    return a**2

testList = [1, -4, 8, -9]

applyToEach(testList, squirred)

print(testList)
