print("WELCOME TO THE USUAL BMI CALCULATOR!")

def bmival(a, b):
    return a / (b ** 2)

while True:
    userheight = float(input("Enter your height(m): "))
    userweight = float(input("Enter your weight(kg): "))

    bmi = bmival(userweight, userheight)

    if bmi < 18.5:
        print("You're underweight!")
    elif 18.5 <= bmi < 24.9:
        print("You're normal :)")
    elif 25.0 <= bmi < 29.9:
        print("You're overweight!")
    else:
        print("You're obese!")
        
    action = input("Do you want to check another BMI (yes/no): ")
    if action.lower == "yes":
        continue
    else:
        print("Thank you for using our bmi calculator!")
        break