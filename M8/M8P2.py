# M8P2 - First 20 Fibonacci numbers, starting with 1, 1.
first = 1
second = 1
for count in range(20):
    print(first)
    next_number = first + second
    first = second
    second = next_number
