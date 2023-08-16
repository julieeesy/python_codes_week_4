# addition calculator
import math
import os

while True:
    try:
        intNum1 = int(input("Enter FIRST Number: "))
        intNum2 = int(input("Enter SECOND Number: "))
        if intNum2 != 0:
            intAns = intNum1 + intNum2
            print(f"{intNum1} + {intNum2} = {intAns}\n")
        else:
            print("Invalid input.\n")
    except ValueError:
        print("Invalid Input.\n")
        os.system('clear')

