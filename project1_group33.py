# Authors: group 33
#   Elias Haneborg 
#   Nithusha Lions
#   Mustafa Arslan
#   Sandra Nestor 

from random import randrange

def getNumberInput():
    inp = input("Enter a number between 1 and 1000: ")
    if not inp.isnumeric():
        print("Invalid input. Try again.")
        return getNumberInput()
    guess = int(inp)
    if guess < 1 or guess > 1000:
        print("Your guess is out of range. Try again")
        return getNumberInput()
    return guess


def play():
    randomNum = randrange(1, 1000)

    attempts = 0
    while True:    
        attempts += 1
        guess = getNumberInput()
        if guess == randomNum:
            print("Congratulation! You guessed the number in %d attempt(s)" % (5 - attempts))
            break
        elif guess < randomNum:
            print("Your guess is too low.")
        elif guess > randomNum:
            print("Your guess is too high.")

        if attempts == 5:
            print("Sorry!! You did not manage to guess the number. You have reached the guessing limit. The answer is %d" % (randomNum))
            break
        else:
            print("You have %d attempt(s) left." % (5 - attempts))

print("Welcome to the number guessing game!")
play()

while True:    
    inp = input("Would you like to play again? ('YES' or 'NO'): ").upper()
    if inp == "YES":
        play()
    elif inp == "NO":
        print("Thank you for playing.")
        break
    else:
        print("'%s' is not a valid option. Type 'YES' or 'NO'." % (inp))