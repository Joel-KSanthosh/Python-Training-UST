class Celsius:
    def __init__(self,fahrenheit : float) -> None:
        self.fahrenheit = fahrenheit
        
    @property
    def celcius(self) -> float:
        return (self.fahrenheit - 32) * 5/9
    
    def __str__(self) -> str:
        return f"Celcius Temperature = {self.celcius}"
    

    
class Kelvin:
    def __init__(self,fahrenheit) -> None:
        self.fahrenheit = fahrenheit
    
    @property
    def kelvin(self) -> float:
        return Celsius(self.fahrenheit).celcius+273.15
    
    def __str__(self) -> str:
        return f"Kelvin Temperature ={self.kelvin}"
    

class Fahrenheit:
    def __init__(self,fahrenheit) -> None:
        self.fahrenheit = fahrenheit
    
        print("[1]. Convert to Celcius\n[2]. Convert to Kelvin\n[3]. Exit")
        choice : int = int(input("Enter a choice : "))
        match choice:
            case 1 : Celsius(self.fahrenheit)
            case 2 : Kelvin(self.fahrenheit)
            case 3 : exit()
            case _ : return "Enter a valid choice !!\n"
    
    def __str__(self) -> str:
        return self.__str__
    
if __name__ == '__main__':
    while(1):
        value : int = int(input("Enter the fahrenheit temperature : "))
        temperature_converter = Fahrenheit(value)
        print(temperature_converter)