numList : int = list(map(int,input("Enter the list of Integers : ").split()))

for i in range(len(numList)-1):
    for j in range(i+1,len(numList)):
        if(numList[i]>numList[j]):
            numList[i],numList[j] = numList[j],numList[i]

print(f"Second largest element = {numList[-2]}")