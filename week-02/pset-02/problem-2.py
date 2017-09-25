
def debtPayoff(balance, annualInterestRate):
    currentBalance = balance
    monthlyPayment = 0
    while currentBalance>0:
        currentBalance = balance
        monthlyPayment += 10
        for i in range(12):
            currentBalance = currentBalance - monthlyPayment
            currentBalance = currentBalance + (annualInterestRate/12 * currentBalance)
    return monthlyPayment

print("Lowest Payment:", debtPayoff(balance, annualInterestRate))
