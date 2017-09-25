
def debtPayoff(balance, annualInterestRate):
    currentBalance = balance
    monthlyInterestRate = annualInterestRate/12
    lowerPayment = balance/12
    upperPayment = (balance * (1 + monthlyInterestRate)**12)/12
    guess = (upperPayment + lowerPayment)/2
    count = 0
    while currentBalance > 0.01 :
        count += 1
        for i in range(12):
            currentBalance = currentBalance - guess
            currentBalance = currentBalance + (annualInterestRate/12 * currentBalance)
        if currentBalance < 0 :
            upperPayment = guess
            guess = (upperPayment + lowerPayment)/2
            currentBalance = balance
        elif currentBalance > 0.01:
            lowerPayment = guess
            guess = (upperPayment + lowerPayment)/2
            currentBalance = balance
    return(round(guess, 2))

print("Lowest Payment:",debtPayoff(balance, annualInterestRate))
