# M4P3 - Meal tips
meal_total = float(input("Enter the total for the meal: "))

tip15 = meal_total * 0.15
tip18 = meal_total * 0.18
tip20 = meal_total * 0.20
total15 = meal_total + tip15
total18 = meal_total + tip18
total20 = meal_total + tip20

print("With 15% Tip:")
print(f"Total: {meal_total:.2f}")
print(f"Tip: {tip15:.2f}")
print(f"Total with Tip {total15:.2f}")
print()
print("With 18% Tip:")
print(f"Total: {meal_total:.2f}")
print(f"Tip: {tip18:.2f}")
print(f"Total with Tip {total18:.2f}")
print()
print("With 20% Tip:")
print(f"Total: {meal_total:.2f}")
print(f"Tip: {tip20:.2f}")
print(f"Total with Tip {total20:.2f}")
