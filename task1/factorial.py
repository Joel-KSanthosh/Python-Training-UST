def fact(number:int):
    if(number==1 or number==0):
        return 1
    else:
        return number * fact(number-1)
        

number : int = int(input("Enter a number : "))

print(f'Factorial = {fact(number)}')