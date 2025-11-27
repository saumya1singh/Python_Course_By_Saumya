# Write a program that prints the sum of first n natural numbers.
# For example, if n = 5, then output should be 1 + 2 + 3 + 4 + 5 = 15.

n= int(input("Enter a number: "))
sum= 0

while n>=1:
    sum= sum+n
    n= n-1

print("Sum= ", sum)
print("n= ", n)



