# Write a program to print this pattern using a while loop:
# *
# * *
# * * *
# * * * *

n= 1

while n<=4:
    print("*" * n)
    n= n+1

print("We are out of the while loop, and value of n should be 5. Is it 5? check : ", n)
