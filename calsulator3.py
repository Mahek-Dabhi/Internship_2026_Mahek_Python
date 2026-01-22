from functions1 import add, subtract, square 

print("Select operation:")
print("1. Additon")
print("2. Subtraction")
print("3. Square of number")

choice = int(input("Enter your choice (1-2-3) :"))

if choice == 1:
    add()
elif choice == 2:
    subtract()
elif choice == 3:
    square()
else:
    print("Invalid choice")
