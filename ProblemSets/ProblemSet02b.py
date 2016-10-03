#Problem Set 2b - Paying Off Credit Card Debt
#Paying of a Credit Card Balance - Paying Debt Off in a Year

balance = 3926 #the outstanding balance on the credit card
annualInterestRate = 0.2 #annual interest rate as a decimal

#code for test..
monthlyInterestRate = annualInterestRate/12 #gives us the monthly interest rate
minMontlhyPayment = 10 #starting monthly minimum payments
runningBalance = balance #getting a copy of the original balance for a running balance checks

while runningBalance > 0: #if it is 0 or below, we will pay it off in the year!
    minMontlhyPayment += 10 #adds a value of $10 to each monthly minimum payment - CAN HAVE THIS AT LITTLE AS 0.01 BUT MUCH MORE COMPUTATION
    runningBalance = balance #reset the running balance back to original balance
    for ans in range(1,13): #do the calculations - 12 months worth of minimum payments with interest to get our ending balance
        unpaidBalance = runningBalance - minMontlhyPayment
        runningBalance = unpaidBalance + (monthlyInterestRate*unpaidBalance)
#required ending print
print("Lowest Payment: " + str(minMontlhyPayment))