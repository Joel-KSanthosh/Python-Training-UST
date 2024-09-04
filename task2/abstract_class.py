from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def get_fuel_efficiency(self) -> str:
        pass
    
    def describe(self) -> None:
        print(f"This is a {self.__class__.__name__}")
        
    
    @classmethod
    def from_name(cls,value : str):
        if value == "car":
            car = Car()
            car.describe()
            print(car.get_fuel_efficiency())
        elif value == "truck":
            truck = Truck()
            truck.describe()
            print(truck.get_fuel_efficiency())
        else:
            raise ValueError("Unknown vehicle type")
            
class Car(Vehicle):
    def get_fuel_efficiency(self):
        return "Fuel efficiency = 25 miles per gallon"
        
class Truck(Vehicle):
    def get_fuel_efficiency(self):
        return "Fuel efficiency = 15 miles per gallon"
        
if __name__ == '__main__':
    
    while(1):
        print("Choices are : car,truck,exit")
        choice = input("Enter a choice : ")
        match choice:
            case "car" : Vehicle.from_name("car")
            case "truck" : Vehicle.from_name("truck")
            case "exit" : exit()
            case _ : print("Enter a valid choice !!")
        
        print()
        