def swapper(num1 : int, num2 : int):
    return num2,num1
    
def bubble_sort():
    myList = list(map(int,input("Enter a list of integers : ").split()))
    
    for i in range(len(myList)):
        for j in range(len(myList)-i-1):
            if(myList[j]>myList[j+1]):
                myList[j],myList[j+1] = swapper(myList[j],myList[j+1])
            
    print(f"Sorted list = {myList}")
    
bubble_sort()