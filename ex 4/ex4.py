4--1
def convert(num):
  b=0
  i=1
  while num!=0:
    r=num%2
    num=num//2
    b=b+i*r
    i=i*10
  return (b)
num=int(input('enter number '))
print('The binary of',num,'is',convert(num))

4--2
def pytrip(m,n):
  for x in range (m,n+1):
    for y in range (x,n+1):
      for z in range(y,n+1):
         if x*x+y*y==z*z:
             print(x,y,z)
l=int(input('enter lower range '))
u=int(input('enter upper range '))
print('The pythagorean triplets are')
pytrip(l,u)

4--3
def fib(n):
   if n<=1:
     return n
   else:
     return(fib(n-1)+fib(n-2))
m=int(input('enter number of terms '))
print('The fibonacci series upto',m,'terms are')
for i in range(m):
   print(fib(i))

4--4
def fact(n):
   if n<=1:
     return 1
   else:
     return n*fact(n-1)

def permut(n,r):
   nPr=fact(n)/fact(n-r)
   return nPr

def comb(n,r):
   nCr=fact(n)/(fact(n-r)*fact(r))
   return nCr

print('1.permutation')
print('2.combination')
choice=int(input('enter your choice '))
if choice==1 or choice==2:
  n=int(input('enter the value of n '))
  r=int(input('enter the value of r '))
  if choice==1:
    print(n,'P',r,'=',permut(n,r))
  elif choice==2:
     print(n,'C',r,'=',comb(n,r))
else:
  print('invalid choice')
