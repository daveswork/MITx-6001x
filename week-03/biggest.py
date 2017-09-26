def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    longest = 0
    longest_key = None
    for k in aDict:
        if len(aDict[k]) > longest:
            longest_key = k
    return longest_key

animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}
empty = {}
print(biggest(animals))
