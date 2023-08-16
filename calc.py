# making a calculator
import math

print("Choose to calculate.\n( + | - | / | * )")

while True:
    choice = input("\nEnter choice: ")
    input_one = int(input("Enter first number: "))
    input_two = int(input("Enter second number: "))
    if '+' in choice:
        result = input_one + input_two
        print(f"{input_one} + {input_two} = {result}\n")
    elif '-' in choice:
        result = input_one + input_two
        print(f"{input_one} - {input_two} = {result}\n")
    elif '*' in choice:
        result = input_one * input_two
        print(f"{input_one} * {input_two} = {result}\n")
    elif '/' in choice:
        result = input_one * input_two
        print(f"{input_one} * {input_two} = {result}\n")
    elif '0' in choice:
        print("Ending program. Goodbye.")
        break

