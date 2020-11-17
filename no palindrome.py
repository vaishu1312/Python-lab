a=int(input('enter the no'))
b=a
rev=0
while a>0:
       rem=a%10
       rev=rem+rev*10
       a=a//10
if (b==rev):
   print('pal')
else:
   print('not a pal')

#reverse a no using recursion
rev=0
def reverse(n):
       global rev
       if n>0:
          rem=n%10
          rev=rem+rev*10
          reverse(n//10)
       return rev
a=int(input('enter the no'))
b=a
r=reverse(b)
if (r==a):
   print('pal')
else:
   print('not a pal')

#palindrome in a range
l=int(input('enter lower limit '))
u=int(input('enter upper limit '))
for i in range(l,u+1):
       b=i
       rev=0
       while i>0:
          rem=i%10
          rev=rem+rev*10
          i=i//10
       if (b==rev):
           print(b,'pal')
       else:
            print(b,'not a pal')


#first n palindromes
n=int(input('enter no '))
count=0
potentialpal=1

def pal(n):
       b=n
       rev=0
       while n>0:
              rem=n%10
              rev=rem+rev*10
              n=n//10
       if (b==rev):
          return True
       else:
          return False

while count<n:
    if pal(potentialpal)== True:
        print ('Palindrome',count + 1, 'is', potentialpal)
        count += 1
        potentialpal += 1
    else:
        potentialpal += 1




