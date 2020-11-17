#recursion-range
def prime(n,div=None):
    if div is None:
        div = n - 1
    while div >= 2:
        if n % div == 0:
            return False
        else:
            return prime(n, div-1)
    else:
        print(n,'is prime')
        return 'True'
l=int(input('enter lower range '))
u=int(input('enter upper range '))
print('Prime nos between',l,'and',u,'are: ')
for i in range(l,u+1):
        prime(i)

#recursion
def prime(n,div=None):
    if div is None:
        div = n - 1
    while div >= 2:
        if n % div == 0:
            print("Number is composite")
            return False
        else:
            return prime(n, div-1)
    else:
        print("Number is prime")
        return True
n=int(input('enter number '))
prime(n)


#
n=int(input('enter number '))
if n>1:
        for j in range(2,n):
                if(n%j==0):
                  print(n,'is composite')
                  break        
        else:
          print(n,'is prime')
elif n==1:
        print('1 is neither prime nor composite')


#FIRST N PRIME NOS-1
n=int(input('enter no '))
count=0
potentialprime = 2

def primetest(n):
    for j in range(2,n):
            if(n%j==0):
                  return False        
    else:
        return True
        
while count<n:
    if primetest(potentialprime) == True:
        #print (potentialprime,'is prime')
        print ('Prime',count + 1, 'is', potentialprime)
        count += 1
        potentialprime += 1
    else:
        #print (potentialprime,'is composite')
        #count+=1
        potentialprime += 1

#FIRST N PRIME NOS-2
n=int(input('enter no '))
count=0
potentialprime = 2     
while count<n:
    for j in range(2,potentialprime):
            if(potentialprime%j==0):
                  break        
    else:
        print('Prime',count + 1, 'is', potentialprime)
        count += 1
    potentialprime += 1

#list
l=int(input('Enter lower range '))
u=int(input('Enter upper range '))
list=[]
prime=[]
comp=[]
for k in range(l,u+1):
    list.append(k)
print('the list of nos is',list)
for num in list:
    for j in range(2,num):
        if(num%j==0):
          comp.append(num)
          break        
    else:
         prime.append(num)
print('The prime nos in the range are',prime)
print('The composite nos in the range are',comp)


l=int(input('enter lower range '))
u=int(input('enter upper range '))
print('Prime nos between',l,'and',u,'are: ')
for i in range(l,u+1):
    if i>1:
      for j in range(2,i):
        if(i%j==0):
          break        
      else:
         print(i)
    elif i==1:
        print('1 is neither prime nor composite')

l=int(input('enter lower range'))
u=int(input('enter upper range'))
for i in range(l,u+1):
    counter=0
    for j in range(2,i):
        if(i%j==0):
            counter=counter+1
    if(counter==0):
       print(i,'is prime')
    else:
       print(i,'is composite')
            




    
