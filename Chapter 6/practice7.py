# Write a program to print the multiplication table of any number using a while
# loop.
# (Hint: Start i = 1 and run the loop until i <= 10.)

n= int(input("Enter a number : "))
i= 1

while i<=10:
    print(f"{n} x {i} = {n*i} ")
    i= i+1