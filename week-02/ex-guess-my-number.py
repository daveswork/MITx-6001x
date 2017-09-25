
ans = ''
guess= 50
upper = 100
lower = 0
print('Please think of a number between 0 and 100!')
while ans != 'c':
    print('Is your secret number '+str(guess))
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if ans == 'l':
        lower = guess
        guess = guess + (upper - lower)//2
    elif ans == 'h':
        upper = guess
        guess = lower + (upper - lower)//2
    elif ans == 'c':
        break
    else:
        print('Sorry, I did not understand your input.')

print('Game over. Your secret number was: '+str(guess))
