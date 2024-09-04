from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self,name) -> None:
        self.name = name
    
    @abstractmethod
    def calculate_salary(self) -> str:
        pass
    
    def describe(self) -> None:
        print(f"My name is {self.name}. I am a {self.__class__.__name__}")
    
class FullTimeEmployee(Employee):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def calculate_salary(self):
        return "$3000"
    
class PartTimeEmployee(Employee):
    def __init__(self, name) -> None:
        super().__init__(name)
        
    def calculate_salary(self) -> str:
        hours_worked = int(input("Enter the hours worked : "))
        hourly_rate = float(input("Enter the hourly rate : "))
        return f"${hours_worked*hourly_rate}"
    
if __name__ == '__main__':
    while(1):
        print("choices = full,part,exit")
        choice = input("Enter a choice : ")
        match choice:
            case "exit" : exit()
            case "full" : 
                name = input("Enter employee name : ")
                full = FullTimeEmployee(name)
                full.describe()
                print(full.calculate_salary())
            case "part" :
                name = input("Enter employee name : ")
                part = PartTimeEmployee(name)
                part.describe()
                print(part.calculate_salary())
            case _:
                print("Enter a valid choice !!")
        print()