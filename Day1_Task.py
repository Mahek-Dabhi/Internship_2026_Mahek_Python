name = input("Enter student name: ")
age = int(input("Enter student age: "))
marks = float(input("Enter student marks: "))

if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
elif marks >= 50:
    grade = 'E'
else:
    grade = 'F'

print("\n" + "-"*40)
print("STUDENT REPORT CARD")
print("-"*40)
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Marks: {marks}")
print(f"Grade: {grade}")
print("-"*40)

if grade in ['A', 'B']:
    print("Performance: Excellent!")
elif grade in ['C', 'D']:
    print("Performance: Good")
elif grade == 'E':
    print("Performance: Needs Improvement")
else:
    print("Performance: Requires Attention")