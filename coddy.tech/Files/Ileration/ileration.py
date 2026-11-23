#Ilerating over elements/sequences
# Read comma-separated input and split it into a list of strings
lst = input().split(",")

# Create an empty list to store words longer than 5 characters
new_lst = []

# Loop through each word in the original list
for word in lst:
    # Check if the character count is strictly greater than 5
    if len(word) > 5:
        # Add the matching word to the new list
        new_lst.append(word)

# Print the filtered list
print(new_lst)
