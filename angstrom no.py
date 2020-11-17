#angstrom no
n=int(input('enter a no '))
a=n
c=0
while a>0:
    c+=1
    a=a//10
#no of digits=c
s=0
a=n
while a>0:
    l=a%10
    s=s+(l**c)
    a=a//10
if s==n:
    print('angstrom no')
else:
    print('not an angstrom no')

#angstrom no in range
l=int(input('enter lower limit '))
u=int(input('enter upper limit '))
for i in range(l,u+1):
    a=i
    c=0
    while a>0:
        c+=1
        a=a//10
    s=0
    a=i
    while a>0:
        l=a%10
        s=s+(l**c)
        a=a//10
    if s==i:
        print(i,'angstrom no')

#first n angstrom no
        
n=int(input('enter no '))
count=0
potentialang=1

def ang(n):
    a=n
    c=0
    while a>0:
        c+=1
        a=a//10
    s=0
    a=n
    while a>0:
        l=a%10
        s=s+(l**c)
        a=a//10
    if s==n:
        return True
    else:
        return False

while count<n:
    if ang(potentialang)== True:
        print ('angstrom no',count + 1, 'is', potentialang)
        count += 1
        potentialang+= 1
    else:
        potentialang+= 1
    
    
