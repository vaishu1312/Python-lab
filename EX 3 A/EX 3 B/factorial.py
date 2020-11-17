#factorial using for loop
n=int(input('enter the number '))
if n==0:
      print('the factorial of',n,'is',1)
elif n<1:
      print('invalid input')
else:      
  fact=1
  #count=1
  for i in range(1,n+1):
  #while count<n+1:
      #fact=fact*count
      fact=fact*i
      #count+=1
  print('the factorial of',n,'is',fact)

#factorial using function
def fact(x):
      if x==0:
         print('the factorial of',x,'is ',end='')
         return 1
      elif x<0:
         return 'invalid input'
      else:
          fact=1
          for i in range(1,n+1):
             fact=fact*i
          print('the factorial of',n,'is ',end='')
          return fact
                
n=int(input('enter the number '))
print(fact(n))     

#factorial using recursive function
def factr(x):
      if x<=1:
         return 1
      else:
          return x*factr(x-1)

n=int(input('enter the number '))
if n<0:
      print('invalid input')
else:
      print('the factorial of',n,'is ',factr(n)) 
      
