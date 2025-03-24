numbers = [float(input(f"Enter number {i+1}: ")) for i in range(10)]
print("The sum of the ten numbers is:", sum(numbers))

numbers = [float(input(f"Enter number {i+1}: ")) for i in range(10)]
print("The maximum number is:", max(numbers))

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"Factorial of {num} is {factorial(num)}")


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):  # Check divisibility from 2 to n-1
        if n % i == 0:
            return False
    return True

# User input
num = int(input("Enter a number: "))

# Check if prime
if is_prime(num):
    print(f"{num} is a Prime number.")
else:
    print(f"{num} is NOT a Prime number.")

