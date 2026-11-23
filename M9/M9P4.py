def pay_rate(jobCode):
    if jobCode == "L":
        return 25
    elif jobCode == "A":
        return 30
    elif jobCode == "J":
        return 50
    return 0


totalGrossPay = 0
again = "Y"
while again == "Y":
    lastName = input("Enter employee last name: ")
    jobCode = input("Enter job code (L, A, J): ").upper()
    hours = float(input("Enter hours worked: "))
    rate = pay_rate(jobCode)
    if hours > 40:
        grossPay = 40 * rate + (hours - 40) * rate * 1.5
    else:
        grossPay = hours * rate
    print("Employee:", lastName)
    print("Gross pay: $", format(grossPay, ".2f"))
    totalGrossPay = totalGrossPay + grossPay
    again = input("Enter Y to continue or N to stop: ").upper()
print("Total gross pay: $", format(totalGrossPay, ".2f"))
