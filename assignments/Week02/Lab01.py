"""
BMI Calculator (20 points)

Write a program that:

Asks for weight in kilograms
Asks for height in meters
Calculates BMI using formula: BMI = weight / (height²)
Displays BMI with 1 decimal place
Shows BMI category based on the ranges below

BMI Categories:

Below 18.5: Underweight
18.5 - 24.9: Normal weight
25.0 - 29.9: Overweight
30.0 and above: Obese

"""

weight = input("Enter your weight in kilograms:" )
height = input("Enter your height in meters:" )
weight = float(weight)
height = float(height)
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.1f}")
if bmi < 18.5:
    print("BMI Category: Underweight")
elif 18.5 <= bmi < 25.0:
    print("BMI Category: Normal weight")
elif 25.0 <= bmi < 30.0:
    print("BMI Category: Overweight")
else:
    print("BMI Category: Obese")
    