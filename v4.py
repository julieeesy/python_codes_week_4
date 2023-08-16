import random
intAnswer = random.randint(10000, 99999)
intGuess = 1

while intGuess != 0:
    try:
        intGuess = int(input("enter your guess or 0 to exit: "))

        # the guess is too high
        if intAnswer < intGuess:
            print("your guess", intGuess, "is TOO HIGH.\n")
        elif intAnswer > intGuess:
            print("your guess", intGuess, "is TOO LOW.\n")
        elif intAnswer == intGuess:
            print("your guess", intGuess, "is CORRECT")
            break
    except ValueError:
        print("wrong input. please input an integer.\n")
