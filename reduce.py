#myreduce
#product of elements in list
def myreduce(func,alist):
    result=alist[0]
    for j in alist[1:]:
        result=func(result,j)
    return result
        
print(myreduce(lambda x,y:x*y,[1,2,3,4]))


#gcd for more than two nos
from functools import reduce
gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
alist=[12,24,32,72,48]
print('The gcd is ',end='')
print(reduce(gcd,alist))

#min val in list
from functools import reduce
min = lambda a, b: a if a<b else b
alist=[12,24,32,72,48]
print('The min value is  ',end='')
print(reduce(min,alist))

#average using reduce
from functools import reduce
alist=[1,2,3,4,5]
print('The average is ',end='')
sum=reduce(lambda a,b:a+b,alist)
print(sum/5)



