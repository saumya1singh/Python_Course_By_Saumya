print("Welcome to BMI Calculator!!!")

weight = float(input("enter your weight in kg: "))
height = float(input("enter your height in m: "))

bmi = weight / (height ** 2)
print(round(bmi, 2))

if(bmi < 18.5):
    print("underweight")
elif(18.5 <= bmi < 25):
    print("normal weight")
else:
    print("overweight")