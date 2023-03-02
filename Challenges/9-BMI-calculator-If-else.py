# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m).

"""
Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
"""
# Warning you should round the result to the nearest whole number.
# The interpretation message needs to include the words
# from the interpretations above. e.g. underweight, normal weight,
# overweight, obese, clinically obese.
"""
Example Input
weight = 85
height = 1.75
Example Output
85 ÷ (1.75 x 1.75) = 27.755102040816325
Your BMI is 28, you are slightly overweight.
"""
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi_result = round(weight / height ** 2)
if bmi_result < 18.5:
    print(f"Your BMI is {bmi_result}, you are underweight.")
elif bmi_result < 25:
    print(f"Your BMI is {bmi_result}, you have a normal weight.")
elif bmi_result < 30:
    print(f"Your BMI is {bmi_result}, you are slightly overweight.")
elif bmi_result < 35:
    print(f"Your BMI is {bmi_result}, you are obese.")
else:
    print(f"Your BMI is {bmi_result}, you  are clinically obese.")