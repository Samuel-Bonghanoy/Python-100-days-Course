height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI = float(weight / height ** 2)

if BMI <= 18.5:
    print(f"Your BMI is {int(round(BMI, 0))}, you are underweight.")
elif BMI <= 25:
    print(f"Your BMI is {int(round(BMI, 0))}, you have a normal weight.")
elif BMI <= 30:
    print(f"Your BMI is {int(round(BMI, 0))}, you are slightly overweight.")
elif BMI <=35:
    print(f"Your BMI is {int(round(BMI, 0))}, you are obese.")
elif BMI > 35:
    print(f"Your BMI is {int(round(BMI, 0))}, you are clinically obese.")

