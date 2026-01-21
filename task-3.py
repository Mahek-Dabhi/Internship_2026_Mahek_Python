numbers = []

n = int(input("How many numbers do you want to enter : "))

for i in range(n):
    numbers.append(int(input("Enter number: ")))

print("Addition of the numbers is : ", sum(numbers))

sub = numbers[0]
for i in numbers[1:]:
    sub -= i
print("Subtraction of the numbers is : ", sub)

print("Square of numbers is : ")
for i in numbers:
    print(i, ":", i*i)