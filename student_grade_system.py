# Student Grade Management System

student_name = input("Enter student name: ")
score = int(input("Enter student score: "))

if score >= 70 and score <= 100:
    grade = "A"
elif score >= 60:
    grade = "B"
elif score >= 50:
    grade = "C"
elif score >= 40:
    grade = "D"
else:
    grade = "F"

print("\n--- Student Result ---")
print("Name:", student_name)
print("Score:", score)
print("Grade:", grade)
