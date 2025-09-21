""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
class vehicle:

    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year 

    def get_info(self):
        return f"vehicle : {self.brand},{self.model},{self.year}"
    
class Car(vehicle):

    def __init__(self, brand, model, year,number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def get_info(self):
        return f"Brand:{self.brand},Model:{self.model},Year:{self.year},Doors:{self.number_of_doors}"
    
V1 = vehicle("Ferrari","F40","1987")
print(V1.get_info())

c1 = Car("Honda","FK8","2022")
print(c1.get_info())