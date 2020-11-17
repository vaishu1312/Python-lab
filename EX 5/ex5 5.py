import string
print('1.case of string/2.octal & hexadecimal digits')
ch=int(input('Enter choice '))
if ch==1:
   str=input('Enter string ')
   x=str.replace(' ','')
   for i in x:
     a=i in string.ascii_lowercase
     if a==False:
        break
   if a==True:
     print('In lower case')
   else:
        print('Not in lower case')
elif ch==2:
    print('The octal digits are ',string.octdigits)
    print('The hexadecimal digits are ',string.hexdigits)
else:
   print('Invalid choice')

