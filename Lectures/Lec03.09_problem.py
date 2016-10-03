#Number guesser between 1 and 100 - Bisection search method
guess = 0 #need to define this first or the while loop won't be able to check against it.
high = 100
low = 0
ans = (high + low)/2 #first answer is always 50
print("Please think of a number between 0 and 100!") #prompt the user!
while guess != str("c"):
    print("Is your secret number " + str(ans) + "?")
    guess = str(raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly: "))
    if guess == str("c"):
        break #breaks the while lopp as we have the answer
    elif guess == str("h"):
        high = ans
        ans = (high + low)/2
    elif guess == str("l"):
        low = ans
        ans = (high + low)/2
    elif guess != str("h") or str("l") or str("c"):
        print("Sorry, I did not understand your input.") #Check to make sure only h, l or c have been inputted.
print("Game over. Your secret number was: " + str(ans))
