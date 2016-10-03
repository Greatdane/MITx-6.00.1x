#Problem Set 2c - Paying Off Credit Card Debt,
#Paying of a Credit Card Balance - Paying Debt Off in a Year - Bisection search method!

balance = 320000 #the outstanding balance on the credit card
annualInterestRate = 0.2 #annual interest rate as a decimal

#code for test
monthlyInterestRate = annualInterestRate/12 #gives us the monthly interest rate
high = (balance * (1 + monthlyInterestRate)**12)/12 #high payment
low = balance / 12 #not zero - has to be at least a 12th of the balance (even with no interest)
minMontlhyPayment = (high + low)/2
precision = 0.01 #how accurate do you want the answer. 0.01 is to the cent.

def calculation(balance, montlhyPayment):
    '''
    Calulation function does 12 months worth of monthly payments with interest to get our ending balance
    '''
    global calculationBalance #creates a global variable named calculationBalance
    for ans in range(1,13):
        unpaidBalance = balance - montlhyPayment
        balance = unpaidBalance + (monthlyInterestRate*unpaidBalance)
    calculationBalance = balance #assigns the global variable to the current balance
    return balance

#print("Initial guess is " + str(minMontlhyPayment))  

while abs(calculation(balance, minMontlhyPayment)) >= precision : #gets an absolute number and checks if it matches the variable precision
    if calculationBalance > 0: #if the calculationBalance given out (this is why we needed it) is higher than 0, the payment is too low to pay off in 12 months
        #print("Guess too low")
        low = minMontlhyPayment
    else:
        #print("Guess too high")
        high = minMontlhyPayment        
    minMontlhyPayment = (high + low)/2
    #print ("trying " + str(minMontlhyPayment))
        
print("Lowest Payment: " + str(round(minMontlhyPayment, 2)))
