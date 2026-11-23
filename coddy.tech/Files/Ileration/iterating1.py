# Read a string from the user
text = input()

# Initialize a counter variable to keep track of 'p' or 'P'
count = 0

# Loop through each character in the string one by one
for char in text:
    # Convert the character to lowercase and check if it equals 'p'
    if char.lower() == "p":
        # Add 1 to the counter if it matches
        count += 1

# Print the final count
print(count)
