# Read comma-separated input and split it into a list
lst = input().split(",")

# Find the middle index using integer division
mid = len(lst) // 2

# Check if the list length is odd (remainder of 1 when divided by 2)
if len(lst) % 2 == 1:
    # Take 1 item before the middle, the middle item, and 1 item after (stop index is exclusive)
    result = lst[mid - 1 : mid + 2]
else:
    # For even-length lists, take the two middle items
    result = lst[mid - 1 : mid + 1]

# Print the resulting slice
print(result)
