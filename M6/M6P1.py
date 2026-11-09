# Module 6, Problem 1: Widget pricing
quantity = int(input("Enter the quantity of widgets: "))

if quantity > 10000:
    price = 10.00
else:
    if quantity >= 5000:
        price = 20.00
    else:
        price = 30.00

extended_price = quantity * price
tax = extended_price * 0.07
total = extended_price + tax

print()
print(f"{'Extended price:':<22}${extended_price:>14,.2f}")
print(f"{'Tax:':<22}${tax:>14,.2f}")
print(f"{'Total:':<22}${total:>14,.2f}")
