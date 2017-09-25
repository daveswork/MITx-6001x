

def balanceForward(balance, annualInterestRate, monthlyPaymentRate):
    currentBalance = balance
    for i in range(12):
        minPayment = monthlyPaymentRate * currentBalance
        currentBalance = currentBalance - minPayment
        interestAccrued = (annualInterestRate / 12) * currentBalance
        currentBalance = currentBalance + interestAccrued
    return round(currentBalance, 2)

print("Remaining balance:", balanceForward(balance, annualInterestRate, monthlyPaymentRate))
