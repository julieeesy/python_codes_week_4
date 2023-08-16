def calculate(nDonuts):
    if nDonuts < 12: # 1.50 each
        individual_Donuts = 1.50 * nDonuts
        dozens_of_donuts = 0

    elif nDonuts >= 12: # 12 for the dozen 1.25 each
        individual_Donuts = 1.25 * (nDonuts - 12)
        dozens_of_donuts = 12.00

    else: # 20 for 2 dozen 1.00 each
        individual_Donuts = 1.00 * (nDonuts - 24)
        dozens_of_donuts = 20.00

    total =  individual_Donuts + dozens_of_donuts
    return total

order1 = calculate(6)
print(order1)
order2 = calculate(11)
print(order2)
print(calculate(13))
print(calculate(25))