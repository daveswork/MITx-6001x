'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
'''

s = 'odtfrqud'


pos = 0
current = s[0]
longest = s[0]
for char in s[1:]:
    pos += 1
    if char >= current[len(current)-1]:
        current= current + char
        if len(current)>len(longest):
            longest = current
    else:
        current = char
print('Longest substring in alphabetical order is:', longest)
