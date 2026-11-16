# M7P2 - Display a sequence using a while loop.
start = int(input("Enter the start value: "))
stop = int(input("Enter the stop value: "))
increment = int(input("Enter the increment: "))

if increment == 0:
    print("The increment cannot be zero.")
elif start < stop and increment < 0 or start > stop and increment > 0:
    print("The increment must move toward the stop value.")
else:
    number = start
    while (increment > 0 and number <= stop) or (increment < 0 and number >= stop):
        print(number)
        number = number + increment
