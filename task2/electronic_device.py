from abc import ABC, abstractmethod
from random import randint,uniform

class ElectronicDevice(ABC):
    def __init__(self,brand,model) -> None:
        self.brand = brand
        self.model = model
      
    @abstractmethod
    def power_usage(self) -> None:
        pass
      
    def describe(self) -> None:
        print(f"Brand = {self.brand} and Model = {self.model}")
        
    @classmethod
    def from_type(cls,value : str,brand : str,model : str):
        if value == "laptop":
            laptop = Laptop(brand,model)
            laptop.describe()
            laptop.power_usage()
            print(laptop.battery_life)
        elif value == "phone":
            phone = SmartPhone(brand,model)
            phone.describe()
            phone.power_usage()
            print(phone.screen_size)
        else:
            print("Unknown Device")
            

class Laptop(ElectronicDevice):
    def __init__(self, brand, model) -> None:
        super().__init__(brand, model)
        
    battery_life = f"Battery life = {randint(0,100)}%"
        
    def power_usage(self):
        print("Power usage = 50 watts per hour")

class SmartPhone(ElectronicDevice):
    def __init__(self, brand, model) -> None:
        super().__init__(brand, model)
        
    screen_size = f"Screen size = {uniform(3,6.6)} inches"
    
    def power_usage(self):
        print("Power usage = 10 watts per hour")
        
if __name__ == '__main__':
    while(1):
        print("Choices = phone,laptop,exit")
        choice = input("Enter a choice : ")
        if(choice == "exit"):
            break
        
        brand = input("Enter a brand : ")
        model = input("Enter a model : ")
        ElectronicDevice.from_type(choice,brand,model)
        
        print()
        