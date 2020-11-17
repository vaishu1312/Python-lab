#transpose
X=[[1,2,3],[4,5,6],[7,8,9]]
t=[]
for i in range(len(X)):
    t.append([])
    for j in range(len(X[0])):
        t[i].append(X[j][i])
print(t)
        
#LC
X=[[1,2,3],[4,5,6],[7,8,9]]
t=[[X[j][i] for j in range(len(X[0]))] for i in range(len(X))]
print(t)
    
