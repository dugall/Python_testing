#4: Class Inheritance
#Create a Bus class that inherits from the Vehicle class.
#Give the capacity argument of Bus.seating_capacity() a default value of 50.
#Use the following code for your parent Vehicle class.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
	def seating_capacity(self, capacity = 50):
		return super().seating_capacity(capacity = 50)

#https://www.scaler.com/topics/super-in-python/
# Child Class
#class Car(Vehicle):
#  def __init__(self, company, model, year, color, car_type):
    # Using super to access __init__ method of Parent Class
#    super().__init__(company, model, year, color)
#    self.car_type = car_type

# Creating an object of Car
#my_car = Car("Tesla", "S", 2021, "Silver", "Sedan")
#print(f"I have a {my_car.company} model {my_car.model}.")


Schoolbus = Bus("School_Volvo", 180, 12)

print(Schoolbus.seating_capacity())

#print ("Vehicle Name:", Schoolbus.name, "Speed:", Schoolbus.max_speed, "Mileage:", Schoolbus.mileage, "capacity", seating_capacity)