m=int(input('enter lower range '))
n=int(input('enter upper range '))
pt=[(x,y,z) for x in range (m,n+1) for y in range (x,n+1) for z in range(y,n+1) if x*x+y*y==z*z]
print(pt)

X=[[1,2,3],[4,5,6],[7,8,9]]
l=[]
for i in range(len(X)):
    for j in range(len(X[i])):
        l.append(X[i][j])

print(l)
#flatten alist
X=[[1,2,3],[4,5,6],[7,8,9]]
l=[j for i in X for j in i]
print(l)
    
#lc
#perfect square
#prime no
n=int(input('enter no '))
c=[n for i in range(2,n) if(n%i==0)]
print(c)

#prime range
l=int(input('enter lower range '))
u=int(input('enter upper range '))
c=[i for i in range(l,u+1) for j in range(2,i) if(i%j==0)]
p=[i for i in range(l,u+1) if i not in c]
print(c)
print(p)

#f to c
c=[100,101,102,103,104]
f=[(9/5)*x+32 for x in c]
print(f)
#mat mul
r=[[sum(m1[i][k]*m2[k][j] for k in range(ca)) for j in range(cb)] for i in range(ra)]
#mat add
r=[[m1[i][j]+m2[i][j] for j in range(ca)] for i in range(ra)
#transpose
X=[[1,2,3],[4,5,6],[7,8,9]]
t=[[X[j][i] for j in range(len(X[0]))] for i in range(len(X))]
print(t)

