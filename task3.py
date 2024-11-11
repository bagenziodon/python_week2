# Task 3: Dictionary to store personal information and print it

# Create an empty dictionary
person_info = {}

# Ask for user input to populate the dictionary
person_info["name"] = input("Enter your name: ")
person_info["age"] = int(input("Enter your age: "))
person_info["favorite_color"] = input("Enter your favorite color: ")

# Print the dictionary
print("\nInformation about the person:")
print(person_info)
