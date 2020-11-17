# Matrix Multiplication
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

# Function - Matrix Multiplication
def fn_mul(MA, MB, ra, ca, cb):
    M = []
    for i in range(0,ra):
        M.append([])
        for j in range(0,cb):
            ele = 0
            for k in range(0,ca,1):
                ele = ele + (MA[i][k] * MB[k][j])
            M[i].append(ele)
    return M


# Main Program

print("Enter number of rows and columns :")
r1 = int(input("Matrix 1 - Row : "))
c1 = int(input("Matrix 1 - Column : "))
r2 = int(input("Matrix 2 - Row : "))
c2 = int(input("Matrix 2 - Column : "))

# Multiplication
if (c1 != r2):
    print("Rows and columns do not match.")
    print("Cannot multiply.")
else:
    Mat_A = fn_read(r1, c1)
    Mat_B = fn_read(r2, c2)
    
    print("Given matrix 1 : ")    
    fn_display(Mat_A)
    print("Given matrix 2 : ")    
    fn_display(Mat_B)
        
    Mat_Mul = fn_mul(Mat_A, Mat_B, ra = r1, ca = c1, cb = c2)
    print("Product of given matrices : ")
    fn_display(Mat_Mul)
