myList : str = input("Enter a list of numbers : ").split()

mySet : str = set(myList)

myDict = { key : 0 for key in mySet}

for letter in myList:
    if(letter in mySet):
        myDict[letter] += 1
    
for key,value in myDict.items():
    print(f'frequency of {key} = {value}')
    