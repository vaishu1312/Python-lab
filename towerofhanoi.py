def towerofhanoi(n,beg,end,aux):
    if n==1:
         print('move disc',n,'from rod',beg,'to rod',end)
         return
    else:
        towerofhanoi(n-1,beg,aux,end)
        print('move disc',n,'from rod',beg,'to rod',end)
        towerofhanoi(n-1,aux,end,beg)
n=int(input('enter no of disks '))
towerofhanoi(n,'A','C','B')
             
        
