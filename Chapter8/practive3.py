# Read only the first line of bio.txt

with open("bio.txt", "r") as f:
    line1= f.readline()
    print("Line 1", line1)

