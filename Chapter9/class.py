#class creation 
class Vehicle:
    color="black" #attributes
    petrolOrDiesel="petrol" #attributes
    mileage="10" #attributes

    def start():    #methods
        print("When you press clutch and accelerator then vehicle is started")


#object creation
car= Vehicle()
car.color= "pink"
print(car.color)

bike= Vehicle()
print(bike.color)

aeroplane= Vehicle()
print(aeroplane.mileage)
print(aeroplane.color)


#we created one class and 3 objects of that class