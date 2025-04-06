class Vehicle:
    def move(self):
        pass  # Base class move method (we'll override it in subclasses)

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Testing polymorphism
vehicles = [Car(), Plane()]

for vehicle in vehicles:
    print(vehicle.move())  # Each vehicle will move differently
