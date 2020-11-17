#
month = input ( 'Enter the name of the month: ')
if month.casefold() == 'april'  or month.casefold() == 'june' or month.casefold() == 'september' or month.casefold() == 'november' :
                print ( 'The no days  in ' , month, 'are  30')
elif month.casefold() == 'february':
                print ('The no of days in february are 28' )
else :
        print ('The no of days in ', month , 'are 31')


#
def  freq ( n, i):
        count  = 0
        while  n> 0:
                    r  = n% 10
                    n = n//10
                    if  r == i:
                          count+=1
        return  count
n = int ( input ( 'Enter the integer: ' ))
for i in  range ( 0, 10 ) :
            x = freq ( n, i )
            if x != 0 :
               print ( 'no of ' , i, " s", ' are: ' , x )

#
n = int ( input ( 'Enter the number: ' ))
(r,m)=(0,0)
print('The no is ',end='')
while n>0:
  l =  n%10
  n = n//10
  r = l+r*10
  m=m+1
for  i in range   (0,m):
         l1 = r%10
         r = r//10
         if l1==1:
              print('one ',end='')
         elif l1==2:
              print('two ', end='')
         elif l1== 3:
              print('three ',end='')
         elif l1== 4:
              print('four ',end='')
         elif l1== 5:
              print('five ',end='')
         elif l1== 6:
              print('six ',end='')
         elif l1== 7:
              print('seven ',end='')
         elif l1== 8:
              print('eight ',end='')
         elif l1== 9:
              print('nine ',end='')
         elif l1== 0:
              print('zero ',end='')


##
str=input('Enter the string ')
ch=0
d=['0','1','2','3','4','5','6','7','8','9']
d1=0
s=['!','@','#','$','%','^','&','*']
s1=0
for i in str:
   if i in s:
     s1+=1
for i in str:
    if i in d:
       d1+=1
for i in str:
    if ('a'<=i<='z' or 'A'<=i<='Z'):
        ch+=1
print('No of characters are : ',ch)
print('No of digits are: ',d1)
print('No of special characters are: ',s1)

#
def lcm(a,b,i):
   if i%a==0 and i%b==0:
            return i
   else:
         i+=1
         return lcm(a,b,i)

a= int ( input ( ' Enter the first no: ' ))
b= int ( input ( ' Enter the second no: ' ))
print('The lcm of ',a,'and',b,'is ',lcm(a,b,1))
