#tuples Basics 

myTuple= (78, 90, 75)
studentTuple= ("Khushi", "Divya", "Ishaan", "Divya")
print(len(myTuple))
# studentTuple[1]= "Aanchal" Tuples are IMMUTABLE/NOT Changeable

print(studentTuple[2])

#empty Tuples
emptyTuple= ()
singleTuple= (1,)
print(type(emptyTuple))
print(type(singleTuple))
print(studentTuple.index("Divya"))
print(studentTuple.count("Aditya"))

