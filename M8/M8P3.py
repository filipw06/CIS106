# M8P3 - Employee bonuses from a text file.
from pathlib import Path

data_path = Path(__file__).resolve().parent / "M8P3_data.txt"
total_bonuses = 0.0
print(f"{'Last Name':<18}{'Salary':>16}{'Bonus':>16}")
with open(data_path, "r") as data_file:
    for last_name in data_file:
        last_name = last_name.strip()
        salary = float(data_file.readline())
        if salary >= 100000:
            bonus_rate = 0.20
        elif salary >= 50000:
            bonus_rate = 0.15
        else:
            bonus_rate = 0.10
        bonus = salary * bonus_rate
        total_bonuses = total_bonuses + bonus
        print(f"{last_name:<18}{'$' + format(salary, ',.2f'):>16}{'$' + format(bonus, ',.2f'):>16}")
print(f"Total bonuses paid: ${total_bonuses:,.2f}")
