# Read comma-separated input and split it into a list
lst = input().split(",")

# 1. Every third element, starting from index 1 (the second element)
slice1 = lst[1::3]

# 2. All elements from the 6th element (index 5) to the 1st (index 0) in reverse order
slice2 = lst[5::-1]

# 3. Every second element starting from the middle of the list to the end
mid = len(lst) // 2
slice3 = lst[mid::2]

# Print the three resulting lists
print(slice1)
print(slice2)
print(slice3)
