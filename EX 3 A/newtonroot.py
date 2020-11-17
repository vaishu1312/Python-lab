#Square root using Newton's Method-recursion
def sqrt(num,approx,better=1):
     approx=better
     better=(approx + num/approx)/2
     if better==approx:
          print("Square root: ",end='')
          return better
     else:
        return sqrt(num,approx,better)

     
num=int(input("Enter no. :"))
approx=num
if num>0:
     print(sqrt(num,approx))
else:
     print('no not positive')
     
#Square root using Newton's Method-function
def sqrt(num):
     if num>0:
          approx=num
          better=1
          while better!=approx:
               approx=better
               better=(approx + num/approx)/2 
          print("Square root: ",end='')
          return better
     else:
          return 'no not positive'
     
num=int(input("Enter no. :"))
print(sqrt(num))

#Square root using Newton's Method
num=int(input("Enter no. :"))
if num>0:
     approx=num
     better=1
     while better!=approx:
          approx=better
          better=(approx + num/approx)/2 
     print("Square root:" , better)
else:
     print('no not positive')
