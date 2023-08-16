while True:
    while True:
        check_in_name = input("Enter your name: ")
        if isinstance(check_in_name, str):
            break
        else:
            print("Retype your name please.")
    check_in_age = input("Enter your age {0}: ".format(check_in_name))
    try:
        val = int(check_in_age)
        if isinstance(val, int):
            print("Your age is {0}".format(val))
            break
    except ValueError:
        print("That's not an int!")