from random import randrange


def play():
    randomNum = randrange(1, 1000)

    attempts = 0
    while True:    
        attempts += 1
        guess = int(input("Enter a number between 1 and 1000: "))
        if guess == randomNum:
            print("You guessed the correct number, congratz.")
            break
        elif guess < randomNum:
            print("Your guess is too low.")
        elif guess > randomNum:
            print("Your guess is too high.")

        if attempts == 5:
            print("Sorry!! you are out of guesses. The answer is %d" % (randomNum))
            break
        else:
            print("You have %d attempt(s) left." % (5 - attempts))

play()

while True:    
    inp = input("Would you like to play again? ('YES' or 'NO'): ").upper()
    if inp == "YES":
        play()
    elif inp == "NO":
        print("Bye Bye.")
        break
    else:
        print("%s is not a valid option. Type 'YES' or 'NO'." % (inp))