number : int = int(input("Enter a number : "))

flag : bool = 1

for i in range(2,number//2):
    if(number % i == 0):
        flag = 0
        break

if(flag == 1 and number != 1):
    print("Prime")
elif(flag == 1 and number == 1):
    print(f'{number} is neither prime nor composite')
else:
    print("Not Prime")