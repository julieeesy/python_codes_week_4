import random
intAnswer = random.randint(10000, 99999)
intGuess = 1
intCount = 0

while intGuess != 0:
    try:
        intGuess = int(input("enter your guess or 0 to exit: "))
        intCount += 1
        print("You have ",intCount, "out of 10.")
        if intCount <= 10:
            # the guess is too high
            if intAnswer < intGuess:
                print("your guess", intGuess, "is TOO HIGH.\n")
            elif intAnswer > intGuess:
                print("your guess", intGuess, "is TOO LOW.\n")
            elif intAnswer == intGuess:
                print("your guess", intGuess, "is CORRECT")
                break
        else:
            print("You have run out of guesses.")
    except ValueError:
        print("wrong input. please input an integer.\n")
