'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
'''

count = 0
for i in range(len(s)-2):
    j = s[i] + s[i+1] + s[i+2]
    if j == 'bob':
        count += 1
print('Number of times bob occurs is:', count)
