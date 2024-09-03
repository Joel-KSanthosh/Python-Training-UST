first = list(input("Enter the first list : ").split())
second = list(input("Enter the second list : ").split())
combined_set = set()

for item in first:
    if(item in second):
        combined_set.add(item)
        
print(f"Common elements are : {combined_set}")