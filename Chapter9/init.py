
class Student:
    schoolName= "ABC School"

    def __init__(self, name, course):
        # print("Whenever a new object is created I am called automaticaly")
        # print(self)
        self.name= name
        self.course= course


student1= Student("Khushi", "Btech") #init method will be called
print("Student1 Name-", student1.name)
print("Student1 Course-", student1.course)

student2= Student("Ankit", "Bsc")
print("Student2 Name-", student2.name)
print("Student2 Course-", student2.course)