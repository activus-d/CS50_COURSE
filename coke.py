"""
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
"""
def coke():
    payment_accumulation = 0

    while payment_accumulation < 50:
        payment = int(input("Insert coin: "))
        if payment in {25, 10, 5}:
            payment_accumulation += payment
            print(f"Amount Due: {50 - payment_accumulation}")
        else:
            print("Invalid coin. Please insert a 5, 10, or 25 cent coin.")

    if payment_accumulation > 50:
        print(f"Change Owed: {payment_accumulation - 50}")
    else:
        print("Enjoy your Coke!")

coke()
