print('1.no of occurrences/2.index of occurrence/',end='')
print('3.right justify/4.Capitalize/5.alphanumeric check')
ch=int(input('enter choice '))
if (ch==1):
  str1=input('enter string ')
  sub=input('enter substring ')
  print ('The no of occurences are ',str1.count(sub))

elif (ch==2):
  str1=input('enter string ')
  sub=input('enter substring ')
  print ('The substring is found at index ',str1.rfind(sub))   

elif (ch==3):
   str1=input('enter string ')
   print (str1.rjust(5))

elif (ch==4):
   str1=input('enter string ')
   print (str1.capitalize())

elif (ch==5):
   str1=input('enter string ')
   a=str1.isalnum()
   if a==True:
      print('The string is alphanumeric')
else:
  print('Invalid choice')

