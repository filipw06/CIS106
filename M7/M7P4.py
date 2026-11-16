# M7P4 - Calculate gross pay, including overtime, and payroll totals.
total_gross_pay = 0.0
employee_count = 0
response = input("Do you want to enter an employee? (Yes to continue): ")
while response.strip().lower() == "yes":
    last_name = input("Enter the employee's last name: ")
    hours = float(input("Enter hours worked: "))
    pay_rate = float(input("Enter hourly pay rate: "))
    if hours > 40:
        gross_pay = 40 * pay_rate + (hours - 40) * pay_rate * 1.5
    else:
        gross_pay = hours * pay_rate
    print(f"Last name: {last_name}")
    print(f"Gross pay: ${gross_pay:,.2f}")
    total_gross_pay = total_gross_pay + gross_pay
    employee_count = employee_count + 1
    response = input("Do you want to enter another employee? (Yes to continue): ")

if employee_count > 0:
    average_pay = total_gross_pay / employee_count
else:
    average_pay = 0.0
print(f"Total gross pay: ${total_gross_pay:,.2f}")
print(f"Number of employees: {employee_count}")
print(f"Average pay: ${average_pay:,.2f}")
