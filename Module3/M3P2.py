# M3P2 - Weighted exam points
# Input: Last name; midterm score (0-100); final exam score (0-100)
# Process: total_exam_points = midterm_score * 0.40 + final_score * 0.60
# Output: Last name; total exam points

last_name = input("Enter your last name: ")
midterm_score = float(input("Enter your midterm score (0-100): "))
final_score = float(input("Enter your final exam score (0-100): "))

total_exam_points = midterm_score * 0.40 + final_score * 0.60

print(f"Student last name: {last_name}")
print(f"Total exam points: {total_exam_points:.2f}")
