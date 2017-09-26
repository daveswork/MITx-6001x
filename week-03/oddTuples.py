
def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    oddReturn = ()
    for i in range(0, len(aTup), 2):
        oddReturn = oddReturn + (aTup[i],)
    return oddReturn
    #
#oddTuple(('I', 'am', 'a', 'test', 'tuple'))

test = ('I', 'am', 'a', 'test', 'tuple')

print(oddTuples(test))
