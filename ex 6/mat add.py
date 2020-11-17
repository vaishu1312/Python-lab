# Function - Matrix Addition
def add(MA, MB):
    r=len(MA)
    c=len(MB)
    M = []
    for i in range(0,r):
        M.append([])
        for j in range(0,c):
            ele = MA[i][j] + MB[i][j]
            M[i].append(ele)
    return M

a=[[1,2,3],[4,5,6],[2,8,9]]
b=[[6,7,8],[2,4,0],[1,2,8]]
ra=len(a)
ca=len(a[0])
rb=len(b)
cb=len(b[0])
if ( (ra != rb) or (ca != cb) ):
    print("Rows and columns of given matrices do not match.")
    print("Cannot Add the matrices.")
else:
    print('The matrix a is ',a)
    print('The matrix b is ',b)
    print(add(a,b))

