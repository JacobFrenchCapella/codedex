
mass = input("Enter your mass in kilograms: ")
height = input("Enter your height in meters: ")
# Calculate BMI
bmi = float(mass) / (float(height) ** 2)
#alternatively, you can use the following line to calculate BMI:
#bmi = float(mass) / (float(height) * float(height))
# Print the result
print(f"Your Body Mass Index (BMI) is: {bmi:.2f}")