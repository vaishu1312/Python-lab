#add
m1=[[1,2,3],[4,5,6],[2,8,9]]
m2=[[6,7,8],[2,4,0],[1,2,8]]
ra=len(m1)
ca=len(m1[0])
rb=len(m2)
cb=len(m2[0])
if ( (ra != rb) or (ca != cb) ):
    print("Rows and columns of given matrices do not match.")
    print("Cannot Add the matrices.")
else:
   r=[[m1[i][j]+m2[i][j] for j in range(ca)] for i in range(ra)]
   print(r)

#mul
m1=[[1,2,3],[4,5,6],[3,0,1]]
m2=[[6,7,8],[2,4,0],[2,0,0]]
ra=len(m1)
ca=len(m1[0])
rb=len(m2)
cb=len(m2[0])
if ca!=rb:
    print("Rows and columns do not match.")
    print("Cannot multiply.")
else:
   r=[[sum(m1[i][k]*m2[k][j] for k in range(ca)) for j in range(cb)] for i in range(ra)] 
   print(r)



