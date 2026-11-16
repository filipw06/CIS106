# M8P5 - Student tuition from a text file.
from pathlib import Path

data_path = Path(__file__).resolve().parent / "M8P5_data.txt"
total_tuition = 0.0
student_count = 0
print(f"{'Last Name':<18}{'Credits':>10}{'Tuition':>18}")
with open(data_path, "r") as data_file:
    for last_name in data_file:
        last_name = last_name.strip()
        district_code = data_file.readline().strip().upper()
        credits = int(data_file.readline())
        if district_code == "I":
            cost_per_credit = 250.0
        elif district_code == "O":
            cost_per_credit = 500.0
        else:
            raise ValueError("District code must be I or O.")
        tuition = credits * cost_per_credit
        total_tuition = total_tuition + tuition
        student_count = student_count + 1
        print(f"{last_name:<18}{credits:>10}{'$' + format(tuition, ',.2f'):>18}")
print(f"Total tuition owed: ${total_tuition:,.2f}")
print(f"Number of students: {student_count}")
