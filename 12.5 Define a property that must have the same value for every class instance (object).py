#5: Define a property that must have the same value for every class instance (object)

class Vehicle:
	color = "Color: White,"
	def __init__(self, name, max_speed, mileage):
		self.name = name
		self.max_speed = max_speed
		self.mileage = mileage
#        self.color = color
#        return super().Vehicle(capacity = "white")
#	def color(self, color):
#		return self.color = "Color: White,"

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

Schoolbus = Bus("School_Volvo", 180, 12)

print (Vehicle.color, "Vehicle Name:", Schoolbus.name, "Speed:", Schoolbus.max_speed, "Mileage:", Schoolbus.mileage)