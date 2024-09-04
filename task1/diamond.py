height = int(input("Enter the height of diamond : "))

for i in range(1,height+1):
    print(" "*(height-i),end="")
    print("*"*(i*2-1))
    
for k in range(height-1,0,-1):
    print(" "*(height-k),end="")
    print("*"*(k*2-1))