# M3P3 - Split job payment
# Input: Total amount received
# Process: amount_per_person = amount_received / 3
# Output: Amount each of the three people receives

amount_received = float(input("Enter the total amount received for the job: "))

amount_per_person = amount_received / 3

print(f"Each person receives: ${amount_per_person:.2f}")
