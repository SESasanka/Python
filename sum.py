# numbers = [float(input(f"Enter number {i+1}: ")) for i in range(10)]
# print("The sum of the ten numbers is:", sum(numbers))

# numbers = [float(input(f"Enter number {i+1}: ")) for i in range(10)]
# print("The maximum number is:", max(numbers))

# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     return fact

# for i in range(5):
#     num = int(input(f"Enter number {i+1}: "))
#     if num < 0:
#         print("Factorial is not defined for negative numbers.")
#     else:
#         print(f"Factorial of {num} is {factorial(num)}")


# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):  # Check divisibility from 2 to n-1
#         if n % i == 0:
#             return False
#     return True

# # User input
# num = int(input("Enter a number: "))

# # Check if prime
# if is_prime(num):
#     print(f"{num} is a Prime number.")
# else:
#     print(f"{num} is NOT a Prime number.")


game_id = ""

player_num = input("Enter your player number (001 to 456): ")

# Validate input
if not (player_num.isdigit() and 1 <= int(player_num) <= 456):
    exit("Invalid input. Please enter a number between 001 and 456.")

player_num = int(player_num)

while player_num > 0:
    symbol_index = player_num % 8  
    game_id = chr(36 + symbol_index) + game_id  
    player_num = player_num // 8  

final_game_id = "ID is : "  + (game_id)
print(final_game_id)
