# M7P3 - Calculate student exam averages and count students.
student_count = 0
response = input("Do you want to enter a student? (Yes to continue): ")
while response.strip().lower() == "yes":
    last_name = input("Enter the student's last name: ")
    exam1 = float(input("Enter exam 1 score: "))
    exam2 = float(input("Enter exam 2 score: "))
    average = (exam1 + exam2) / 2
    print(f"Last name: {last_name}")
    print(f"Average exam score: {average:.2f}")
    student_count = student_count + 1
    response = input("Do you want to enter another student? (Yes to continue): ")

print(f"Number of students: {student_count}")
