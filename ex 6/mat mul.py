def mul(MA, MB, ra, ca, cb):
    M = []
    for i in range(0,ra):
        M.append([])
        for j in range(0,cb):
            ele = 0
            for k in range(0,ca,1):
                ele = ele + (MA[i][k] * MB[k][j])
            M[i].append(ele)
    return M

a=[[1,2,3],[4,5,6],[3,0,1]]
b=[[6,7,8],[2,4,0],[2,0,0]]
ra=len(a)
ca=len(a[0])
rb=len(b)
cb=len(b[0])
if ca!=rb:
    print("Rows and columns do not match.")
    print("Cannot multiply.")
else:
    print('The matrix a is ',a)
    print('The matrix b is ',b)
    print(mul(a,b,ra,ca,cb))



