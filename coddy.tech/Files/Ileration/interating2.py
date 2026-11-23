# Read the text string from the user
text = input()

# Read the delimiter character from the user
delimiter = input()

# Split the text by any whitespace (spaces, tabs, newlines) into a list of words
words = text.split()

# Join the list of words together using the specified delimiter
result = delimiter.join(words)

# Print the final combined string
print(result)
