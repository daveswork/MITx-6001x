def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr)> 1:
        if char == aStr[len(aStr)//2]:
            return True
        else:
            if char > aStr[len(aStr)//2]:
                return isIn(char, aStr[len(aStr)//2:])
            else:
                return isIn(char, aStr[:len(aStr)//2])
    else:
        if char == aStr:
            return True
        else:
            print(len(aStr))
            return False


print(isIn('c', 'abcd'))
