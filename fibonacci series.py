#fibonacci using for loop
n1=0
n2=1
n=int(input('enter no of terms: '))
if n<1:
  print('invalid input')
else:
   print("Fibonacci sequence upto",n,"terms:")
   for i in range(0,n) :
       print(n1)
       c = n1 + n2
       (n1,n2) = (n2,c)
          
#fibonacci using while loop
n1=0
n2=1
n=int(input('enter no of terms: '))
if n<1:
  print('invalid input')
else:
   print("Fibonacci sequence upto",n,"terms:")  
   count=0
   while count < n :
       print(n1)
       c = n1 + n2
       (n1,n2) = (n2,c)
       count += 1

#fibonacci using function
def fibo(x):
    n1=0
    n2=1
    if x<1:
        print('invalid input')
    else:
       print("Fibonacci sequence upto",x,"terms:")
       for i in range(0,x) :
          print(n1)
          c = n1 + n2
          (n1,n2) = (n2,c)
          
n=int(input('enter no of terms: '))
fibo(n)

#fibonacci using recursion
def fibor(x):
    if x<=1:
        return x
    else:
        return(fibor(x-1) + fibor(x-2))
      
n = int(input("Enter number of terms: "))
if n<1:
    print('invalid input')
else:
  print("Fibonacci sequence upto",n,"terms:")
  for i in range(0,n):
     print (fibor(i))


