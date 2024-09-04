def matrix_row_sum():
    row_2d = int(input("Enter no: of rows in 2D list : "))
    col_2d = int(input("Enter no: of columns in 2D list : "))

    matrix = list()

    for r in range(row_2d):
        print(f"Enter the values {r}th row : ", end="")
        matrix.append(list(map(int,input().split())))
        print()

    for i in range(row_2d):
        sum = 0
        for j in range(col_2d):
            sum += matrix[i][j]
        print(f'Sum of {i}th row = {sum}')
        

def list3D():
    row_2d = int(input("Enter no: of rows in 3D list : "))
    col_2d = int(input("Enter no: of columns in 3D list : "))
    height_2d = int(input("Enter height of 3D list : "))
    
    plane = list()
    
    for i in range(row_2d):
        temp = list()
        for j in range(col_2d):
            print(f"Enter the values {i}th row  {j}th col : ", end="")
            temp.append(list(map(int,input().split())))
        plane.append(temp)
        
    for i in range(row_2d):
        sum = 0
        for j in range(col_2d):
            for k in range(height_2d):
                sum+= plane[i][j][k]
        print(f'Sum of {i}th row = {sum}')
    

while(1):
    print("--------START--------")
    print()
    print("[1]. Row sum for 2D List\n[2]. Row sum for 3D List")
    choice : int = int(input("Enter a choice : "))
    print()
    match choice:
        case 1 : matrix_row_sum()
        case 2 : list3D()
        case _ : print("Enter a valid choice !!")

    print("--------END--------")