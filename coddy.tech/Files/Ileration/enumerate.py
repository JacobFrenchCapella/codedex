# Read comma-separated input from the user and split it into a list of strings
lst = input().split(",")

# Create an empty list to store the matching indices
indices = []

# Loop through the list, getting both the position (index) and item (value)
for index, value in enumerate(lst):
    # Convert the string value into an integer for math and comparisons
    num = int(value)
    
    # Check if the number is under 50 OR divisible by 5 (remainder of 0)
    if num < 50 or num % 5 == 0:
        # Add the matching position to the indices list
        indices.append(index)

# Print the final list of matching indices
print(indices)
