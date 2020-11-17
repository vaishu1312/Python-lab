# Matrix Addition
# Function - Read Matrix
def fn_read(r, c):
    M = []
    print("Enter values of Matrix : ") 
    for i in range(0,r):
      M.append([])
      for j in range(0,c):
           print('Enter element for ','row',i+1,'and column',j+1,': ')
           e=int(input())
           M[i].append(e)
    return M

# Function - Display Matrix
def fn_display(M):
    for row in M:
        for ele in row:
            print(ele, end=" ")
        print()

# Function - Matrix Addition
def fn_add(MA, MB, r, c):
    M = []
    for i in range(0,r):
        M.append([])
        for j in range(0,c):
            ele = MA[i][j] + MB[i][j]
            M[i].append(ele)
    return M

# Main Program

print("Enter number of rows and columns :")
r1 = int(input("Matrix 1 - Row : "))
c1 = int(input("Matrix 1 - Column : "))
r2 = int(input("Matrix 2 - Row : "))
c2 = int(input("Matrix 2 - Column : "))

# Addition
if ( (r1 != r2) or (c1 != c2) ):
    print("Rows and columns of given matrices do not match.")
    print("Cannot Add the matrices.")
else:
    Mat_A = fn_read(r1, c1)
    Mat_B = fn_read(r2, c2)
    
    print("Given matrix 1 : ")    
    fn_display(Mat_A)
    print("Given matrix 2 : ")    
    fn_display(Mat_B)
    
    Mat_Add = fn_add(Mat_A, Mat_B, r1, c1)
    print("Sum of given matrices : ")    
    fn_display(Mat_Add)
