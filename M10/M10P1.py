def forecast_sales(month, sales):
    month = month.lower()[:3]
    if month in ("jan", "feb", "mar"):
        percent = 0.10
    elif month in ("apr", "may", "jun"):
        percent = 0.15
    elif month in ("jul", "aug", "sep"):
        percent = 0.20
    elif month in ("oct", "nov", "dec"):
        percent = 0.25
    else:
        raise ValueError("Enter a valid month.")
    return sales * (1 + percent)

again = input("Do you want to enter sales? (Yes or No): ").lower()
while again == "yes":
    last_name = input("Enter last name: ")
    month = input("Enter month: ")
    sales = float(input("Enter sales: "))
    try:
        next_sales = forecast_sales(month, sales)
        print("Last Name:", last_name)
        print("Next Month Forecast: $", format(next_sales, ".2f"))
    except ValueError as error:
        print(error)
    again = input("Do you want to enter sales? (Yes or No): ").lower()
