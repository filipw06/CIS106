# Module 5, Problem 3: Book orders and shipping
number_of_books = int(input("Enter the number of books: "))
cost_per_book = float(input("Enter the cost per book: "))

order_total = number_of_books * cost_per_book

if order_total > 50.00:
    shipping_charge = 0.00
else:
    shipping_charge = 25.00

print(f"Order total: ${order_total:.2f}")
print(f"Shipping charge: ${shipping_charge:.2f}")
