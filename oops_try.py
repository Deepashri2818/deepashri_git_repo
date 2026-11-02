class Car:
    #Class attribute (shared by all cars)
    wheels = 4
    
    #Constructor (used to create objects)
    def __init__(self, brand, model):
        self.brand = brand #Instance attribute
        self.model = model #Instance attribute
        
    #Method (action)      
    def display_info(self):
        print(f"Brand: {self.brand} Model: {self.model} has {self.wheels} wheels")

#Creating an object of class Car        
my_car = Car("Toyota", "Corolla")        

#Calling a method
my_car.display_info()


#print
# print(my_car.brand)  #Instance Attributes
# print(my_car.wheels)
# print(my_car.model)
# print(Car.wheels) #Class attribute