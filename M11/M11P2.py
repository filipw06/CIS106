def exam_results(exam1, exam2, exam3):
    total_points = exam1 + exam2 + exam3
    average = total_points / 3
    return total_points, average

last_name = input("Enter student last name: ")
exam1 = float(input("Enter exam 1 score: "))
exam2 = float(input("Enter exam 2 score: "))
exam3 = float(input("Enter exam 3 score: "))

total, average = exam_results(exam1, exam2, exam3)
print("Student:", last_name)
print("Total points:", format(total, ".2f"))
print("Average exam score:", format(average, ".2f"))
