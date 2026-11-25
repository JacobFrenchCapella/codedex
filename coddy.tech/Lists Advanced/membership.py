# Splits each input string into a list, using commas as separators
lst1 = input().split(",")
lst2 = input().split(",")

# Write your code below
result = [item for item in lst1 if item not in lst2]
print(result)