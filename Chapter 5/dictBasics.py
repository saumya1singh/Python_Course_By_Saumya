# Dictionary Basics 

student= {
    "name": "Saumya Singh",
    "city": "Sultanpur",
    "age": 25,
    "rollNumber": 23,
}

print(type(student))
print(student["name"])
print(student)
print(student["city"])
# student["city"]= "Hyderabad"
# print(student)
student["favSubject"]= "Maths"
print(student)
student.pop("favSubject")
print(student)
print(student.items())
