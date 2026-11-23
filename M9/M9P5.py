def compute_tuition(creditHours, districtCode):
    if districtCode == "I":
        return creditHours * 250
    elif districtCode == "O":
        return creditHours * 550
    return 0


totalTuition = 0
again = "Y"
while again == "Y":
    lastName = input("Enter student last name: ")
    creditHours = int(input("Enter credit hours: "))
    districtCode = input("Enter district code (I or O): ").upper()
    tuition = compute_tuition(creditHours, districtCode)
    print("Student:", lastName)
    print("Tuition owed: $", format(tuition, ".2f"))
    totalTuition = totalTuition + tuition
    again = input("Enter Y to continue or N to stop: ").upper()
print("Total tuition owed: $", format(totalTuition, ".2f"))
