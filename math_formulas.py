#The Pythagorean theorem states that in a right triangle, the square of the length of the hypotenuse (c) is equal to the sum of the squares of the lengths of the other two sides (a and b). The formula is: c^2 = a^2 + b^2
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

c = a **2 + b **2
#you can use the following line to calculate c:
#c = (a **2 + b **2) **0.5 or math.sqrt(a **2 + b **2)
c = c **0.5
print(f"The value of c is: {c}")

def quadratic_formula(a, b, c):
    # Calculate the discriminant
    discriminant = b ** 2 - 4 * a * c
    # Check if the discriminant is positive, negative, or zero
    if discriminant > 0:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root,
    else:
        return None

def main():
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))
    x1 = -b + (b ** 2 - 4 * a * c) ** 0.5 / (2 * a)
    x2 = -b - (b ** 2 - 4 * a * c) ** 0.5 / (2 * a)
    print(f"The roots of the quadratic equation are: {x1} and {x2}")