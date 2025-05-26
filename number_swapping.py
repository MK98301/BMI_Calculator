#Program to swap two numbers

num_1 = input("Enter first number:")
num_2 = input("Enter second number:")

print(f"Numbers before swapping are: \nFirst Number: {num_1}\nSecond Number: {num_2}")

num_3 = num_1
num_1 = num_2
num_2 = num_3

print(f"Numbers after swapping are: \nFirst Number: {num_1}\nSecond Number: {num_2}")