
# Function Definition with Parameters
def average(a=10,b=20):
    averageValue= (a+b)/2
    print(averageValue)


# Function Calling with Arguments 
average(5, 10)
average(7, 10)
average(80, 98)
average()

# Write a function show_age(name, age) that prints: "Saumya Singh is 21
# years old."

def show_age(name="Saumya Singh", age= 25):
    print(f"{name} is {age} years old")

show_age("Saumya Singh", 25)
show_age()
show_age("Divya", 19)

