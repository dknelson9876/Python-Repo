

def hideLetterA(str):
    toreturn = ""
    for i in range(0, len(str)):
        if str[i]=='a':
            toreturn += "*"
        else:
            toreturn += str[i]

    return toreturn

def hasMoreEvenThanOdd(str):
    oddCount = 0
    evenCount = 0

    for i in range(0, len(str)):
        if int(str[i]) % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1

    return evenCount > oddCount

def makeTextTriangle(height):
    toreturn = ""
    for row in range(0, height):
        for i in range(0, row):
            toreturn += "*"
        toreturn += "\n"
    return toreturn

