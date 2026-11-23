def sales_report(sales):
    if sales > 100000:
        commission = sales * 0.10
    else:
        commission = sales * 0.05
    next_year_target = sales * 0.05
    return commission, next_year_target

last_name = input("Enter salesperson last name: ")
sales = float(input("Enter sales: "))
commission, target = sales_report(sales)
print("Salesperson:", last_name)
print("Commission: $", format(commission, ".2f"))
print("Next year's target: $", format(target, ".2f"))
