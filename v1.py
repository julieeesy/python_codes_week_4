import os
answer = 12345
print("Welcome!")
print("Try guessing a number and test ur luck :>\n")

while True:
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess == answer:
                os.system('clear')
                print("You guessed right! Congratulations!\n")
                break
            else:
                os.system('clear')
                print("Sorry incorrect, try guessing another number.\n")
        except ValueError:
            os.system('clear')
            print("Wrong input! Try, again.")
    try:
        go_again = input("Do you want to go again? (yes/no): ")
        if 'yes' in go_again:
            os.system('clear')
            print("Cleared screen!\n")
            continue
        elif 'no' in go_again:
            print("\nThank you for playing!")
            break
        else:
            print("\nWrong input!\nThank you for playing!")
            break
    except ValueError:
        print("Erroring!!!!")
