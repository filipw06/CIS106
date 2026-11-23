total = 0
tax = 0

def calculate_total_and_tax(qty, unit_price):
    global total, tax
    total = qty * unit_price
    tax = total * 0.07

qty = int(input("Enter quantity: "))
unit_price = float(input("Enter unit price: "))
calculate_total_and_tax(qty, unit_price)
print("Total: $", format(total, ".2f"))
print("Tax: $", format(tax, ".2f"))
