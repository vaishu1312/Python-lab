#1-3+5-7+9-11+13-15
n=15
print('1',end='')
sign=1
for i in range(3,n+1,2):
        sign=-sign
        if sign==-1:
            print(i*sign,sep='',end='')
        else:
            print('+',i,sep='',end='')

print()
#1+3-5+7-9+11-13+15
n=15
print('1',end='')
sign=-1
for i in range(3,n+1,2):
        sign=-sign
        if sign==-1:
            print(i*sign,sep='',end='')
        else:
            print('+',i,sep='',end='')
    

print()
#1+2-3+4-5+6-7+8-9+10-11+12-13+14-15
n=15
print('1',end='')
for i in range(2,n+1):
    if i%2==0:
        print('+',i,sep='',end='')
    else:
        print('-',i,sep='',end='')

print()
#1-2+3-4+5-6+7-8+9-10+11-12+13-14+15
n=15
print('1',end='')
for i in range(2,n+1):
    if i%2==0:
        print('-',i,sep='',end='')
    else:
        print('+',i,sep='',end='')


