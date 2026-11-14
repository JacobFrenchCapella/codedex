# Replace the two zeros below so that the if condition is true
a = 23
b = 11

# Don't change below this line
c = 0
if a >= b and not b < 10:
    #The not command is an invert of what expression is being sad
    #in this example, it means B must be greater than 10
    c = 2

c += 1
print(f"c = {c}")
#The output must be 3 instead of 1.