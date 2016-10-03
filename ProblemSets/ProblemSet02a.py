#Problem Set 2a - Paying Off Credit Card Debt
#Paying of a Credit Card Balance - Paying the Minimum

balance = 4842 #the outstanding balance on the credit card
annualInterestRate = 0.2 #annual interest rate as a decimal
monthlyPaymentRate = 0.04 #minimum monthly payment rate as a decimal

#code for test..
totalPaid = 0 #define Total paid first
for ans in range(1,13): #loops 12 times for months
    print("Month: " + str(ans))
    minMonthlyPayment = round((balance * monthlyPaymentRate), 2) #calculates min monthly payment to two decimal places
    print("Minimum monthly payment: " + str(minMonthlyPayment))
    balance = balance - minMonthlyPayment #update the balance for the month    
    interest = ((annualInterestRate/12.0) * balance) #apply interest on the remaining balance
    balance = round((balance + interest), 2) #generate a new balance with interest added, to two decimal places
    print("Remaining balance: " + str(balance))
    totalPaid = totalPaid + minMonthlyPayment #keep a tally of the total paid

#ending prints..
print("Total paid: " + str(totalPaid))
print("Remaining balance: " + str(balance))