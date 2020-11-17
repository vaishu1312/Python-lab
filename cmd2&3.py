import sys
print('No of words: ',len(sys.argv)-1)


import sys
f=sys.argv[1:]
if len(f)>2:
  if f[1]=='+':
    print('sum: ',int(f[0])+int(f[2]))
  if f[1]=='-':
    print('difference: ',int(f[0])-int(f[2]))
  if f[1]=='x':
    print('product: ',int(f[0])*int(f[2]))
  if f[1]=='/':
    print('remainder: ',int(f[0])%int(f[2]))
    print('quotient: ',int(f[0])//int(f[2]))
else:
  print('Not enough arguments')
