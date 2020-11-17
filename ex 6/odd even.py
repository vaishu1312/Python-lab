#6--4
l=int(input('enter lower range '))
u=int(input('enter upper range '))
odd=[]
even=[]
list=[]
for k in range(l,u+1):
    list.append(k)
print('The list of numbers are ',list)
for num in list:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print('The list of even numbers are ',even)
print('The list of odd numbers are ',odd)

#first n odd/even nos
n=int(input('enter no'))
count=0
potentialodd=1
def odd(n):
    if n%2!=0:
        return True
    else:
        return False
while count<n:
    if odd(potentialodd)==True:
        print(potentialodd,'is odd')
        count+=1
        potentialodd+=1
    else:
        #print(potentialodd,'is even')
        #count+=1
        potentialodd+=1
        
        
