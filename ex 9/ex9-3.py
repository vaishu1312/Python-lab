file=open('data.txt','w')
file.write('Good morning \n')
file.write('How are you? \n')
file.write('Good bye \n')
file.close()

file=open('data.txt','r')
print(file.read())
x=input('Enter the word to be found: ')
y=input('Enter the word to replace it : ')
print()

file=open('data.txt','r+')
f=file.read()
if x in f:
  f=f.replace(x,y)
  file=open('data.txt','w')
  file.write(f)
  file=open('data.txt','r')
  print(file.read())
else:
    print('The word',x,'is not found')
file.close()


#
f1 = open('data.txt', 'r')
f2 = open('new.txt', 'w')
for line in f1:
  f2.write(line.replace(x,y))
f1.close()
f2.close()





