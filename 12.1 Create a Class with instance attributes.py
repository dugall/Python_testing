#1: Create a Class with instance attributes


class Car:
	def __init__(self, max_speed, mileage):
		self.max_speed = max_speed
		self.mileage = mileage

CN16 = Vehicle(320, 100000)

print (CN16.max_speed, CN16.mileage)