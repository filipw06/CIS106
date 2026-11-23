def calculate_discount(qty, price, discount_rate):
    original_total = qty * price
    discount_amount = original_total * discount_rate
    discounted_price = original_total - discount_amount
    return discount_amount, discounted_price

qty = int(input("Enter quantity: "))
price = float(input("Enter unit price: "))
rate = float(input("Enter discount rate as a percent (e.g. 10): ")) / 100

discount, discounted_price = calculate_discount(qty, price, rate)
print("Quantity:", qty)
print("Unit price: $", format(price, ".2f"))
print("Discount amount: $", format(discount, ".2f"))
print("Discounted price: $", format(discounted_price, ".2f"))
