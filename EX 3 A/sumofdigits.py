#Sum of all digits of a number
n=int(input("Enter number:"))
sum=0
while n >0:
     l=n%10
     sum=sum+l
     n=n//10
print("Sum of the digits:",sum)
