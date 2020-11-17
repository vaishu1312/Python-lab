#no of words,lines,characters in a file
file=open('data.txt','w')
file.write('Good morning \n')
file.write('How are you? \n')
file.write('Good bye \n')
file.close()
lines=0
words=0
char=0
file=open('data.txt','r')
print(file.read())
file=open('data.txt','r')
for i in file:
  lines+=1
  w=i.split()
  words+=len(w)
  for i in w:
    char+=len(i)
file.close()
print('No of lines: ',lines)
print('No of words: ',words)
print('No of characters: ',char)

#command line arg file name
import sys
file=open(sys.argv[1],'r')
lines=0
words=0
char=0
for i in file:
  lines+=1
  w=i.split()
  words+=len(w)
  for i in w:
    char+=len(i)
file.close()
print('No of lines: ',lines)
print('No of words: ',words)
print('No of characters: ',char)



