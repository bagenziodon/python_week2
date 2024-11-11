# Task 5: List comprehension to find words with odd number of characters

# Create a list of words
words = input("Enter a list of words (separated by space): ").split()

# Use list comprehension to find words with odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Print the list of odd length words
print("Words with an odd number of characters:", odd_length_words)
