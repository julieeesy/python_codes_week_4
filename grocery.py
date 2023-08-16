# calling this function so that there is only 1 place to calculate the entire grocery
def calculate(item_list, item_find):
    item_price = float(item_list[item_find + 1])
    item_amount = int(input(f"How many {item_list[item_find]} do you want: "))
    item_cost = item_price * item_amount
    # print(f"{item_cost} item_cost") --> to check if the item cost was placed at the right pace
    items = item_list[item_find] + "(" + str(item_amount) + ")"
    cart_items.append(item_list[item_find])
    return item_cost

fruits = ["apples", 1.50, "oranges", 1.75, "banana", 2.00, "avocado", 2.50, "kiwi", 1.15]
veges = ["onions", 2.50, "cucumber", 5.25, "potatoes", 3.50, "lettuce", 4.50, "salad mix", 4.00]
deli = ["ham", 4.00, "salmon", 8.00, "sausages", 8.00, "salami", 5.50, "mussels", 8.00]

cart_total = 0.0
cart_items = []
cart_price = 0.0

while True:
    print("Choose Department: ")
    print("(D)elicatessen")
    print("(F)ruit Section")
    print("(V)egetables")
    print("e(X)it")
    section_choice = input("Enter Letter: ")
    section_choice = section_choice[0]
    section_choice = section_choice.lower()

    match section_choice:
        case "d":
            print("\nDELICATESSEN SECTION")
            print("(H)am")
            print("(S)almon")
            print("s(A)usages")
            print("sa(L)ami")
            print("(M)ussels")
            deli_choice = input("\nSelect Deli: ")
            deli_choice = deli_choice[0]
            deli_choice = deli_choice.lower()
            # deli_amount = int(input("How many?: "))

            match deli_choice:
                case "h":
                    deli_find = deli.index("ham")
                case "s":
                    deli_find = deli.index("salmon")
                case "a":
                    deli_find = deli.index("sausages")
                case "l":
                    deli_find = deli.index("salami")
                case "m":
                    deli_find = deli.index("mussels")
                case "g":
                    continue

            # deli_price = float(deli[deli_find + 1])
            # deli_cost = deli_amount * deli_price
            # cart_total = cart_total + deli_cost
            # cart_items.append(deli[deli_find])

            deli_cost = calculate(deli, deli_find)
            cart_price = cart_price + deli_cost

            # print(cart_items)
            # print("Cost so far: {0}".format(cart_total))
            # printing 2 decimal places
            print("Cost so far = ${:.2f}".format(cart_price))
            print(f"Cart items = {cart_items}")

        case "f":
            print("\nFRUIT SECTION")
            print("(A)pples")
            print("a(V)ocado")
            print("(B)anana")
            print("(K)iwi")
            print("(O)ranges")
            fruit_choice = input("\nSelect Fruit: ")
            fruit_choice = fruit_choice[0]
            fruit_choice = fruit_choice.lower()
            # fruit_amount = int(input("How many?: "))

            match fruit_choice:
                case "a":
                    fruit_find = fruits.index("apples")
                case "v":
                    fruit_find = fruits.index("avocado")
                case "b":
                    fruit_find = fruits.index("banana")
                case "k":
                    fruit_find = fruits.index("kiwi")
                case "o":
                    fruit_find = fruits.index("oranges")
                case "g":
                    continue

            # fruit_price = float(fruits[fruit_find + 1])
            # fruit_cost = fruit_amount * fruit_price
            # cart_total = cart_total + fruit_cost
            # cart_items.append(fruits[fruit_find])

            fruit_cost = calculate(fruits, fruit_find)
            cart_price = cart_price + fruit_cost

            # print(cart_items)
            # print("Cost so far: {0}".format(cart_total))
            # printing 2 decimal places
            print("Cost so far = ${:.2f}".format(cart_price))
            print(f"Cart items = {cart_items}")

        case "v":
            print("\nVEGETABLE SECTION")
            print("(O)nions")
            print("(C)ucumber")
            print("(P)otatoes")
            print("(L)ettuce")
            print("(S)alad Mix")
            vege_choice = input("\nSelect Vegetable: ")
            vege_choice = vege_choice[0]
            vege_choice = vege_choice.lower()
            # vege_amount = int(input("How many?: "))

            match vege_choice:
                case "o":
                    vege_find = veges.index("onions")
                case "c":
                    vege_find = veges.index("cucumber")
                case "p":
                    vege_find = veges.index("potatoes")
                case "l":
                    vege_find = veges.index("lettuce")
                case "s":
                    vege_find = veges.index("salad mix")
                case "g":
                    continue

            # vege_price = float(veges[vege_find + 1])
            # vege_cost = vege_amount * vege_price
            # cart_total = cart_total + vege_cost
            # cart_items.append(veges[vege_find])

            vege_cost = calculate(veges, vege_find)
            cart_price = cart_price + vege_cost

            # print(cart_items)
            # print("Cost so far: {0}".format(cart_total))
            # printing 2 decimal places
            print("Cost so far = ${:,.2f}".format(cart_price))
            print(f"Cart items = {cart_items}")

        case "x":
            break

        case _:
            break

    break