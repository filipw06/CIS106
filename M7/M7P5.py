# M7P5 - Calculate order discounts and accumulate discount amounts.
total_discounts = 0.0
response = input("Do you want to enter an order? (Yes to continue): ")
while response.strip().lower() == "yes":
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))
    extended_price = quantity * price
    if extended_price > 10000:
        discount_rate = 0.25
    else:
        discount_rate = 0.10
    discount_amount = extended_price * discount_rate
    total = extended_price - discount_amount
    print(f"Extended price: ${extended_price:,.2f}")
    print(f"Discount amount: ${discount_amount:,.2f}")
    print(f"Total: ${total:,.2f}")
    total_discounts = total_discounts + discount_amount
    response = input("Do you want to enter another order? (Yes to continue): ")

print(f"Sum of all discounts: ${total_discounts:,.2f}")
