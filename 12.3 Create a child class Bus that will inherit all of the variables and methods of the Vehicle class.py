#3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
	pass

Schoolbus = Bus("School_Volvo", 180, 12)

print ("Vehicle Name:", Schoolbus.name, "Speed:", Schoolbus.max_speed, "Mileage:", Schoolbus.mileage)
