# M3P4 - Auto discount
# Input: Make; model; MSRP; discount percent as a decimal
# Process: amount_off = msrp * discount_percent; discounted_price = msrp - amount_off
# Output: Make; model; MSRP; discount percent; amount off; discounted price

make = input("Enter the auto make: ")
model = input("Enter the auto model: ")
msrp = float(input("Enter the MSRP: "))
discount_percent = float(input("Enter the discount as a decimal (0.15 for 15%): "))

amount_off = msrp * discount_percent
discounted_price = msrp - amount_off

print(f"Make: {make}")
print(f"Model: {model}")
print(f"MSRP: ${msrp:.2f}")
print(f"Discount percent: {discount_percent:.2%}")
print(f"Amount off: ${amount_off:.2f}")
print(f"Discounted price: ${discounted_price:.2f}")
