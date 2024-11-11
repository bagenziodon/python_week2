
# Task 1: List of integers and compute the sum

# Create an empty list to store integers
numbers = []

# Accept user input and populate the list
num_count = int(input("How many numbers do you want to input? "))
for i in range(num_count):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)

# Compute the sum of all integers
total_sum = sum(numbers)

# Display the sum
print(f"The sum of the numbers is: {total_sum}")