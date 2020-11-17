#gcd of two nos-while loop
n1=int(input("Enter a number: "))
n2=int(input("Enter another number: "))
if n1<n2:
  (n1,n2)=(n2,n1)
rem=n1%n2
while rem!=0:
  (n1,n2)=(n2,rem)
  rem=n1%n2
print ("gcd of given numbers is : ",n2)

#gcd using function
def gcd(a,b):
  if a<b:
    (a,b)=(b,a)
  rem=a%b
  while rem!=0:
    (a,b)=(b,rem)
    rem=a%b
  print("gcd of given numbers is : ",end='')
  return b

n1=int(input("Enter a number: "))
n2=int(input("Enter another number: "))
print(gcd(n1,n2))

#gcd using recursion:
def gcdr(a,b):
    if a<b:
      (a,b)=(b,a)
    if(b==0):
        return a
    else:
        return gcdr(b,a%b)
      
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
print("gcd of given numbers is : ",gcdr(n1,n2))

  


  

    
