#7
def clone(lista):
    listb=lista[:]
    e=int(input('Enter a no '))
    listb.append(e)
    listb.sort()
    print("List 'a' after cloning ",lista)

def alias(lista):
    listb=lista
    e=int(input('Enter a no '))
    listb.append(e)
    listb.sort()
    print("List 'a' after aliasing ",lista)
    
lista=[]
n=int(input('Enter no of nos '))
for i in range(0,n):
    e=int(input('Enter no {} '.format(i+1)))
    lista.append(e)
print('List a outside function is ',lista)
clone(lista)
alias(lista)

          
    
