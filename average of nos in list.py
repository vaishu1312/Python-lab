l=[]
n=int(input('enter no of terms '))
sum=0
for i in range(n):
    a=int(input('enter the no '))
    l.append(a)
    sum=sum+a
print('the list is',l)
avg=sum/n
print(avg)

#using reduce
from functools import reduce
alist=[1,2,3,4,5]
print('The average is ',end='')
sum=reduce(lambda a,b:a+b,alist)
print(sum/5)


