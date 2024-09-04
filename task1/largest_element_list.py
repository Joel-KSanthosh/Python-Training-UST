number : int = list(map(int,input("Enter a list of numbers : ").split()))

max :int = 0
for num in number:
    if(num>max):
        max = num
    
print(f"The largest number = {max}")
