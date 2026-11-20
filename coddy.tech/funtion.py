def print_large_number():
    print("50005000")

n = int(input())
for i in range(n):
    print_large_number()

def square_number(n):
    return n * n

def second_square():
    #This is part 2 of square numbers
    input_num = int(input())
    result = square_number(input_num)
    print(result)

def sigma(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def is_valid(username, password):
    if username == "admin":
        return True
    elif username == "user" and password == "Password123":
        return True
    else:
        return False

def paint(surface, color="blue"):
    #If the surface and color were swap as is, then it will fail.
    print(f"Painting {surface}{color}")

def order(item, quantity=1, express=False):
    print(item, quantity, express)

order("Book", 3)

