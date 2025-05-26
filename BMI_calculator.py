#Program to calculate BMI

weight = float(input("Enter your weight (in kg):"))
height = float(input("Enter your height (in cm):"))

new_height = height/100
final_height = (new_height) ** 2
bmi = weight/final_height
final_bmi = int(bmi)

min_weight = int(18.5 * final_height)
max_weight = int(24.9 * final_height)

print(f"Your BMI value is {final_bmi}")

if(final_bmi <= 18.5):
    print(f"You are Underweight. Your weight should be between {min_weight} and {max_weight}")
elif(18.5 < final_bmi <= 24.9):
    print("You are Healthy")
elif(25 < final_bmi <= 29.9):
    print(f"You are Overweight. Your weight should be between {min_weight} and {max_weight}")
else:
    print(f"You are Obese. Your weight should be between {min_weight} and {max_weight}")