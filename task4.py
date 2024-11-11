# Task 4: Two sets and find common elements

# Create two sets by accepting user input
set1 = set(map(int, input("Enter integers for set 1 (separated by space): ").split()))
set2 = set(map(int, input("Enter integers for set 2 (separated by space): ").split()))

# Find common elements between the two sets
common_elements = set1 & set2

# Print the common elements
print(f"The common elements between the two sets are: {common_elements}")
