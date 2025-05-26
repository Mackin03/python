#Polymorphism

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start(self):
        print("Vehicle is starting")
    
    def stop(self):
        print("Vehicle is stopping")
    
class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels
        
    def start(self):
        print("car is starting...")
    
    def stop(self):
        print("car is stopping...")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels
    
    def start(self):
        print("bike is starting...")
        
    def stop(self):
        print("bike is stopping...")

#Create list of vehicles to inspect
vehicles: list[Vehicle] = [
    Car("Ford", "Focus", 2016, 5, 4),
    Motorcycle("Triumph", "Trident", 2023, 2),
]

#Loop through list of vehiciles and inspect them
for vehicle in vehicles:
    print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
    vehicle.start()
    vehicle.stop()
    
