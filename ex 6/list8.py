#8
def matrix(m):
     for i in range(len(m)):
        for j in range (len(m[0])):
            m[i][j]=(m[i][j])**2            

a=[[1,2,3],[4,5,6],[8,9,0]]
print('The matrix is ',a)
matrix(a)
print('The updated matrix is ',a)

