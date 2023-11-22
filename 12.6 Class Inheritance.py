#6: Class Inheritance
#Create a Bus child class that inherits from the Vehicle class.
#The default fare charge of any vehicle is seating capacity * 100.
#If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.
#So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
    	return self.capacity * 100

class Bus(Vehicle):
	def fare(self):
		total_amount = super().fare()
		total_amount = total_amount * 1.1
		return total_amount

School_bus = Bus("School_Volvo", 180, 50)

print("Total Bus fare is:", School_bus.fare())
