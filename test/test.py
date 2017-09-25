
ans = ''
guess= 50
upper = 100
lower = 0
while ans != 'y':
    ans = input('is your number '+str(guess))
    if ans == 'l':
        lower = guess
        guess = guess + (upper - lower)//2
    if ans == 'h':
        upper = guess
        guess = guess - (upper - lower)//2
