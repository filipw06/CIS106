# M8P4 - Order totals from a text file.
from pathlib import Path

data_path = Path(__file__).resolve().parent / "M8P4_data.txt"
total_extended_price = 0.0
order_count = 0
print(f"{'Item':<18}{'Quantity':>10}{'Price':>14}{'Extended Price':>18}")
with open(data_path, "r") as data_file:
    for item in data_file:
        item = item.strip()
        quantity = int(data_file.readline())
        price = float(data_file.readline())
        extended_price = quantity * price
        total_extended_price = total_extended_price + extended_price
        order_count = order_count + 1
        print(f"{item:<18}{quantity:>10}{'$' + format(price, ',.2f'):>14}{'$' + format(extended_price, ',.2f'):>18}")
if order_count > 0:
    average_order = total_extended_price / order_count
else:
    average_order = 0.0
print(f"Total extended prices: ${total_extended_price:,.2f}")
print(f"Number of orders: {order_count}")
print(f"Average order: ${average_order:,.2f}")
