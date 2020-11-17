#integer to binary conversion
num=int(input('enter num '))
if num < 0:
        print('Must be a positive integer')
elif num==0:
    print ('the binary no of',num,'is','0')
else:
    b=0
    i=1
    a=num
    while num>0:
      r=num%2
      num=num//2
      b+=i*r
      i=i*10
    print ('the binary no of',a,'is',b)
    
#integer to binary conversion-function
def dec2bin(num):
  if num < 0:
        return 'Must be a positive integer'
  elif num==0:
    print ('the binary no of',num,'is',end='')
    return '0'
  else:
    b=0
    i=1
    a=num
    while num>0:
      r=num%2
      num=num//2
      b+=i*r
      i=i*10
    print('the binary no of',a,'is ',end='')
    return b

n=int(input('enter num '))
print(dec2bin(n))

#integer to binary conversion-recursion
def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

num=int(input('enter num '))
print ('the binary no of',num,'is ',end='')
convertToBinary(num) 

#binary rep of n is binary rep of n//2 and 0 if n is divisible by 2 or else  1




