def get_difference(list1, list2):
    # Keep elements in list1 that are not in list2, preserving order
    return [item for item in list1 if item not in list2]

# Example usage
first_list = [10, 20, 30, 40, 50]
second_list = [20, 40, 60]

result = get_difference(first_list, second_list)
print(result)
# Output: [10, 30, 50]
