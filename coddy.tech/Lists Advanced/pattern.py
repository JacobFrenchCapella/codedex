def create_pattern(numbers, repeats):
    # Concatenate the list with itself
    doubled = numbers + numbers
    
    # Repeat the resulting list 'repeats' times
    pattern = doubled * repeats
    
    return pattern
