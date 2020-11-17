n=int(input('enter no '))
sum=1+1/(n+1)
print('the series is')
print('1+',end='')
for i in range(2,n):
    print('1/',i,'+',sep='',end='')
    sum=sum+(1/i)
print('1/',n,sep='')
print('= ',end='')
for j in range(1,n):
    print(1/j,'+',sep='',end='')
print(1/n)    
print('=',sum)



n=int(input('enter no '))
sum=1+(1**(n+1))
print('the series is')
print('1+',end='')
for i in range(2,n):
    print(i,'**2 +',sep='',end='')
    sum=sum+i**2
print(n,'**2',sep='')
print('= ',end='')
for j in range(1,n):
    print(j**2,'+',sep='',end='')
print(n**2)    
print('=',sum)
