print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? "))

tip_percent = float(input("How much tip would you like to give? "))

no_of_people = int(input("How many people to split the bill? "))

tip_amount = (tip_percent/100) * bill
total_bill = bill + tip_amount
spilt_bill = total_bill / no_of_people

print(f"Each person should pay: {round(spilt_bill, 2)}")