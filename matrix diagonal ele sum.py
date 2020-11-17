# Matrix Sum of diagonal elements
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

# Function - Sum of diagonal elements
def fn_add(MA, r):
    s = 0
    for i in range(r):
        s += MA[i][i] 
    return s

# Main Program

print("Enter number of rows and columns :")
r1 = int(input("Matrix 1 - Row : "))
c1 = int(input("Matrix 1 - Column : "))

# Addition and Subtraction
if (r1 != c1):
    print("Not a square matrix.")
    print("Cannot Add the diagonal elements.")
else:
    Mat_A = fn_read(r1, c1)
        
    print("Given Matrix : ")    
    fn_display(Mat_A)
    
    dsum = fn_add(Mat_A, r1)
    print("Sum of diagonal elements of given matrices :", dsum)    
