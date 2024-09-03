prime_list = list()

for i in range(2,101):
    flag = 1
    for j in range(2,i//2):
        if(i%j==0):
            flag = 0
            break
    if(flag == 1):
        prime_list.append(i)

print(f"Prime numbers between 1 - 100 are : {prime_list}")