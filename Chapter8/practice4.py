# Print how many lines are present in notes.txt
import os 

try:
    with open("notes.txt", "r") as f:
        listOfLines= f.readlines()
        print("Output of readLines Function", listOfLines)
        print("Number of Lines in File", len(listOfLines))
except:
    print("That files does not exist")

# RENAMING THE FILE 

# os.rename("report2.txt", "khushi.txt")
# os.remove("khushi.txt")