import sys
file=open(sys.argv[0],'r')
lines=0
words=0
for i in file:
  lines+=1
  w=i.split()
  words+=len(w)
print('The no of words are ',words)
