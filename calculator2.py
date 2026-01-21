a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def add(a, b):
    print("\naddition is:", a + b)

def subtract(a, b):
    print("\nsubtraction is:", a - b)

def sqrta(a):
    print("\nsquare of {a} is:", a * a)

def sqrtb(b):
    print("\nsquare is:", b * b)

print("\nChoose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Square of first number")
print("4. Square of second number")

choice = int(input("\nEnter choice (1, 2, 3, 4): "))

if choice == 1:
    add(a, b)
elif choice == 2:
    subtract(a, b)
elif choice == 3:
    sqrta(a)
elif choice == 4:
    sqrtb(b)
else:
    print("Invalid choice")


